from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def segitiga(request):
    if request.method == 'GET':
        # Retrieve parameters from the request
        input_number = request.GET.get('value')
            # Convert the number to a string
        num_str = str(input_number)

        # Count the number of digits in the number
        num_digits = len(num_str)

        zero_label = 0

        # Initialize the output string
        output = ""

        # Iterate over each digit in the number
        for i, digit in enumerate(num_str):
            # Calculate the number of trailing zeros
            num_zeros = num_digits - i - 1

            zero_label = zero_label + 1

            # Append the digit to the output string
            output += digit

            # Append the trailing zeros to the output string
            output += "0" * zero_label

            # Add a newline character after each line (except the last one)
            if i < num_digits - 1:
                output += "</br>"

        # Return a JSON response
        return JsonResponse({'result': output})


@csrf_exempt
def ganjil(request):
    if request.method == 'GET':
        # Retrieve parameters from the request
        value = request.GET.get('value')
        limit = value
        if limit is not None and limit.isdigit():
            limit = int(limit)
            odd_numbers = [num for num in range(1, limit + 1) if num % 2 != 0]
            return JsonResponse({'odd_numbers': odd_numbers})
        else:
            error_message = 'Invalid input. Please enter a positive integer.'
            return JsonResponse({'error_message': error_message})


        # Return a JSON response
        return JsonResponse({'message': 'Endpoint 1 response'})
    

@csrf_exempt
def prima(request):
    if request.method == 'GET':
        # Retrieve parameters from the request
        limit = request.GET.get('value')
        if limit is not None and limit.isdigit():
                limit = int(limit)
                prime_numbers = []
                for num in range(2, limit + 1):
                    is_prime = True
                    for i in range(2, int(num ** 0.5) + 1):
                        if num % i == 0:
                            is_prime = False
                            break
                    if is_prime:
                        prime_numbers.append(num)
                return JsonResponse({'prime_numbers': prime_numbers})
        else:
                error_message = 'Invalid input. Please enter a positive integer.'
                return JsonResponse({'error_message': error_message})       
 

        # Return a JSON response
        return JsonResponse({'message': 'Endpoint 1 response'})