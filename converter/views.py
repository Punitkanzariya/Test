from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import io
import requests

def home(request):
    return render(request, 'home.html')

def converter_view(request):
    result = None
    if request.method == 'POST':
        value = float(request.POST.get('value'))
        conversion = request.POST.get('conversion')
        
        if conversion == 'km_to_miles':
            converted_value = value * 0.621371
            result = f"{value} km = {converted_value:.2f} miles"
        elif conversion == 'miles_to_km':
            converted_value = value / 0.621371
            result = f"{value} miles = {converted_value:.2f} km"
        elif conversion == 'c_to_f':
            converted_value = (value * 9/5) + 32
            result = f"{value} °C = {converted_value:.2f} °F"
        elif conversion == 'f_to_c':
            converted_value = (value - 32) * 5/9
            result = f"{value} °F = {converted_value:.2f} °C"
        elif conversion == 'kg_to_lb':
            converted_value = value * 2.20462
            result = f"{value} kg = {converted_value:.2f} lb"
        elif conversion == 'lb_to_kg':
            converted_value = value / 2.20462
            result = f"{value} lb = {converted_value:.2f} kg"

    return render(request, 'unit.html', {'result': result})



# All currencies dictionary
CURRENCIES = {
    "AED": "United Arab Emirates Dirham",
    "AFN": "Afghan Afghani",
    "ALL": "Albanian Lek",
    "AMD": "Armenian Dram",
    "ANG": "Netherlands Antillean Guilder",
    "AOA": "Angolan Kwanza",
    "ARS": "Argentine Peso",
    "AUD": "Australian Dollar",
    "AWG": "Aruban Florin",
    "AZN": "Azerbaijani Manat",
    "BAM": "Bosnia-Herzegovina Convertible Mark",
    "BBD": "Barbadian Dollar",
    "BDT": "Bangladeshi Taka",
    "BGN": "Bulgarian Lev",
    "BHD": "Bahraini Dinar",
    "BIF": "Burundian Franc",
    "BMD": "Bermudian Dollar",
    "BND": "Brunei Dollar",
    "BOB": "Bolivian Boliviano",
    "BRL": "Brazilian Real",
    "BSD": "Bahamian Dollar",
    "BTC": "Bitcoin",
    "BTN": "Bhutanese Ngultrum",
    "BWP": "Botswana Pula",
    "BYN": "Belarusian Ruble",
    "BZD": "Belize Dollar",
    "CAD": "Canadian Dollar",
    "CDF": "Congolese Franc",
    "CHF": "Swiss Franc",
    "CLP": "Chilean Peso",
    "CNY": "Chinese Yuan",
    "COP": "Colombian Peso",
    "CRC": "Costa Rican Colón",
    "CUC": "Cuban Convertible Peso",
    "CUP": "Cuban Peso",
    "CVE": "Cape Verdean Escudo",
    "CZK": "Czech Koruna",
    "DJF": "Djiboutian Franc",
    "DKK": "Danish Krone",
    "DOP": "Dominican Peso",
    "DZD": "Algerian Dinar",
    "EGP": "Egyptian Pound",
    "ERN": "Eritrean Nakfa",
    "ETB": "Ethiopian Birr",
    "EUR": "Euro",
    "FJD": "Fijian Dollar",
    "FKP": "Falkland Islands Pound",
    "GBP": "British Pound Sterling",
    "GEL": "Georgian Lari",
    "GHS": "Ghanaian Cedi",
    "GIP": "Gibraltar Pound",
    "GMD": "Gambian Dalasi",
    "GNF": "Guinean Franc",
    "GTQ": "Guatemalan Quetzal",
    "GYD": "Guyanaese Dollar",
    "HKD": "Hong Kong Dollar",
    "HNL": "Honduran Lempira",
    "HRK": "Croatian Kuna",
    "HTG": "Haitian Gourde",
    "HUF": "Hungarian Forint",
    "IDR": "Indonesian Rupiah",
    "ILS": "Israeli New Shekel",
    "INR": "Indian Rupee",
    "IQD": "Iraqi Dinar",
    "IRR": "Iranian Rial",
    "ISK": "Icelandic Króna",
    "JMD": "Jamaican Dollar",
    "JOD": "Jordanian Dinar",
    "JPY": "Japanese Yen",
    "KES": "Kenyan Shilling",
    "KGS": "Kyrgystani Som",
    "KHR": "Cambodian Riel",
    "KMF": "Comorian Franc",
    "KPW": "North Korean Won",
    "KRW": "South Korean Won",
    "KWD": "Kuwaiti Dinar",
    "KYD": "Cayman Islands Dollar",
    "KZT": "Kazakhstani Tenge",
    "LAK": "Laotian Kip",
    "LBP": "Lebanese Pound",
    "LKR": "Sri Lankan Rupee",
    "LRD": "Liberian Dollar",
    "LSL": "Lesotho Loti",
    "LYD": "Libyan Dinar",
    "MAD": "Moroccan Dirham",
    "MDL": "Moldovan Leu",
    "MGA": "Malagasy Ariary",
    "MKD": "Macedonian Denar",
    "MMK": "Myanma Kyat",
    "MNT": "Mongolian Tugrik",
    "MOP": "Macanese Pataca",
    "MRU": "Mauritanian Ouguiya",
    "MUR": "Mauritian Rupee",
    "MVR": "Maldivian Rufiyaa",
    "MWK": "Malawian Kwacha",
    "MXN": "Mexican Peso",
    "MYR": "Malaysian Ringgit",
    "MZN": "Mozambican Metical",
    "NAD": "Namibian Dollar",
    "NGN": "Nigerian Naira",
    "NIO": "Nicaraguan Córdoba",
    "NOK": "Norwegian Krone",
    "NPR": "Nepalese Rupee",
    "NZD": "New Zealand Dollar",
    "OMR": "Omani Rial",
    "PAB": "Panamanian Balboa",
    "PEN": "Peruvian Nuevo Sol",
    "PGK": "Papua New Guinean Kina",
    "PHP": "Philippine Peso",
    "PKR": "Pakistani Rupee",
    "PLN": "Polish Zloty",
    "PYG": "Paraguayan Guarani",
    "QAR": "Qatari Rial",
    "RON": "Romanian Leu",
    "RSD": "Serbian Dinar",
    "RUB": "Russian Ruble",
    "RWF": "Rwandan Franc",
    "SAR": "Saudi Riyal",
    "SBD": "Solomon Islands Dollar",
    "SCR": "Seychellois Rupee",
    "SDG": "Sudanese Pound",
    "SEK": "Swedish Krona",
    "SGD": "Singapore Dollar",
    "SHP": "Saint Helena Pound",
    "SLL": "Sierra Leonean Leone",
    "SOS": "Somali Shilling",
    "SRD": "Surinamese Dollar",
    "STN": "São Tomé and Príncipe Dobra",
    "SVC": "Salvadoran Colón",
    "SYP": "Syrian Pound",
    "SZL": "Swazi Lilangeni",
    "THB": "Thai Baht",
    "TJS": "Tajikistani Somoni",
    "TMT": "Turkmenistani Manat",
    "TND": "Tunisian Dinar",
    "TOP": "Tongan Paʻanga",
    "TRY": "Turkish Lira",
    "TTD": "Trinidad and Tobago Dollar",
    "TWD": "New Taiwan Dollar",
    "TZS": "Tanzanian Shilling",
    "UAH": "Ukrainian Hryvnia",
    "UGX": "Ugandan Shilling",
    "USD": "United States Dollar",
    "UYU": "Uruguayan Peso",
    "UZS": "Uzbekistani Som",
    "VES": "Venezuelan Bolívar Soberano",
    "VND": "Vietnamese Dong",
    "VUV": "Vanuatu Vatu",
    "WST": "Samoan Tala",
    "XAF": "Central African CFA Franc",
    "XAG": "Silver Ounce",
    "XAU": "Gold Ounce",
    "XCD": "East Caribbean Dollar",
    "XDR": "Special Drawing Rights",
    "XOF": "West African CFA Franc",
    "XPF": "CFP Franc",
    "YER": "Yemeni Rial",
    "ZAR": "South African Rand",
    "ZMW": "Zambian Kwacha",
    "ZWL": "Zimbabwean Dollar"
}

def currency_converter_view(request):
    context = {}
    context['currencies'] = CURRENCIES
    result = None
    from_currency = ''
    to_currency = ''
    amount = ''
    input  = ''

    if request.method == 'POST':
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        amount = request.POST.get('amount')

        try:
            amount_float = float(amount)    
            url = f'https://open.er-api.com/v6/latest/{from_currency}'
            response = requests.get(url)
            data = response.json()

            if data['result'] == 'success':
                rates = data['rates']
                if to_currency in rates:
                    converted_amount = amount_float * rates[to_currency]
                    input = f"{amount_float:.2f} {from_currency}"
                    result = f"{converted_amount:.2f} {to_currency}"
                else:
                    result = "Invalid target currency."
            else:
                result = "Failed to get exchange rates."

        except ValueError:
            result = "Invalid amount."

    context.update({
        'result': result,
        'from_currency': from_currency,
        'to_currency': to_currency,
        'amount': amount,
        'input' : input,
    })

    return render(request, 'currency.html', context)



def number_system_converter(request):
    result = ''
    input_value = ''
    selected_conversion = ''
    conversion_options = [
        'Decimal to Binary',
        'Binary to Decimal',
        'Decimal to Hexadecimal',
        'Hexadecimal to Decimal',
    ]

    if request.method == 'POST':
        selected_conversion = request.POST.get('conversion_type')
        input_value = request.POST.get('value', '').strip()

        try:
            if selected_conversion == 'Decimal to Binary':
                result = bin(int(input_value))[2:]
            elif selected_conversion == 'Binary to Decimal':
                result = str(int(input_value, 2))
            elif selected_conversion == 'Decimal to Hexadecimal':
                result = hex(int(input_value))[2:].upper()
            elif selected_conversion == 'Hexadecimal to Decimal':
                result = str(int(input_value, 16))
            else:
                result = 'Invalid conversion type'
        except ValueError:
            result = 'Invalid input value'

    context = {
        'conversion_options': conversion_options,
        'selected_conversion': selected_conversion,
        'input_value': input_value,
        'result': result,
    }

    return render(request, 'number_system_converter.html', context)

from django.shortcuts import render

def hex_to_rgb(hex_value):
    hex_value = hex_value.lstrip('#')
    if len(hex_value) == 6:
        try:
            return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))
        except:
            return None
    return None

def rgb_to_hex(rgb_string):
    try:
        r, g, b = map(int, rgb_string.split(','))
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return '#{:02X}{:02X}{:02X}'.format(r, g, b)
    except:
        return None
    return None

def color_converter(request):
    result = None
    input_value = ''
    conversion_type = ''
    
    if request.method == 'POST':
        conversion_type = request.POST.get('conversion_type')
        input_value = request.POST.get('value')
        
        if conversion_type == 'hex_to_rgb':
            result = hex_to_rgb(input_value)
            result = f"RGB: {result}" if result else "Invalid HEX format!"
        elif conversion_type == 'rgb_to_hex':
            result = rgb_to_hex(input_value)
            result = f"HEX: {result}" if result else "Invalid RGB format!"
    
    return render(request, 'color_converter.html', {
        'result': result,
        'input_value': input_value,
        'selected_conversion': conversion_type
    })

from django.shortcuts import render

from django.shortcuts import render

def health_converter(request):
    # Group conversions
    weight_conversions = ['kg_to_lb', 'lb_to_kg', 'g_to_oz', 'oz_to_g']
    height_conversions = ['cm_to_in', 'in_to_cm', 'm_to_ft', 'ft_to_m']
    temperature_conversions = ['c_to_f', 'f_to_c']
    extra_conversions = ['bmi']

    result = None
    input_value = ''
    conversion_type = ''
    weight = ''
    height = ''
    bmi_result = None
    bmi_error = None

    if request.method == 'POST':
        conversion_type = request.POST.get('conversion')
        input_value = request.POST.get('value')
        weight = request.POST.get('weight', '').strip()
        height = request.POST.get('height', '').strip()

        try:
            if conversion_type == 'bmi':
                if not weight or not height:
                    bmi_error = "Please enter both weight (kg) and height (cm) for BMI."
                else:
                    w = float(weight)
                    h_cm = float(height)
                    h_m = h_cm / 100
                    if h_m <= 0:
                        bmi_error = "Height must be greater than zero."
                    else:
                        bmi_result = round(w / (h_m ** 2), 2)
            else:
                val = float(input_value)
                if conversion_type == 'kg_to_lb':
                    result = round(val * 2.20462, 2)
                elif conversion_type == 'lb_to_kg':
                    result = round(val / 2.20462, 2)
                elif conversion_type == 'g_to_oz':
                    result = round(val * 0.035274, 2)
                elif conversion_type == 'oz_to_g':
                    result = round(val / 0.035274, 2)
                elif conversion_type == 'cm_to_in':
                    result = round(val / 2.54, 2)
                elif conversion_type == 'in_to_cm':
                    result = round(val * 2.54, 2)
                elif conversion_type == 'm_to_ft':
                    result = round(val * 3.28084, 2)
                elif conversion_type == 'ft_to_m':
                    result = round(val / 3.28084, 2)
                elif conversion_type == 'c_to_f':
                    result = round((val * 9/5) + 32, 2)
                elif conversion_type == 'f_to_c':
                    result = round((val - 32) * 5/9, 2)
                else:
                    result = "Conversion not supported."
        except ValueError:
            if conversion_type == 'bmi':
                bmi_error = "Please enter valid numeric values for weight and height."
            else:
                result = "Invalid input! Please enter a number."

    context = {
        'weight_conversions': weight_conversions,
        'height_conversions': height_conversions,
        'temperature_conversions': temperature_conversions,
        'extra_conversions': extra_conversions,
        'result': result,
        'input_value': input_value,
        'conversion_type': conversion_type,
        'weight': weight,
        'height': height,
        'bmi_result': bmi_result,
        'bmi_error': bmi_error,
    }
    return render(request, 'health_converter.html', context)



def image_to_pdf_view(request):
    if request.method == 'POST' and request.FILES.get('image'):
        img_file = request.FILES['image']
        image = Image.open(img_file)

        # Handle transparency if present
        if image.mode in ("RGBA", "LA"):
            background = Image.new("RGB", image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[-1])  # alpha channel
            image = background
        else:
            image = image.convert('RGB')

        pdf_bytes = io.BytesIO()
        image.save(pdf_bytes, format='PDF')
        pdf_bytes.seek(0)

        response = HttpResponse(pdf_bytes, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="converted.pdf"'
        return response

    return render(request, 'imagetopdf.html')