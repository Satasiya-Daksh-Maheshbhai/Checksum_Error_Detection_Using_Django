from django.shortcuts import render

# ================= BINARY ADDITION WITH STEPS =================

def binary_addition_with_steps(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ''
    carry = 0
    step_detail = []

    for i in range(max_len - 1, -1, -1):
        bit_sum = int(a[i]) + int(b[i]) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2

    if carry:
        wrapped = binary_addition_with_steps(result, '1')[0]
        step_detail.append(f"Carry wrap-around: {result} + 1 = {wrapped}")
        result = wrapped

    return result[-max_len:], step_detail


def calculate_checksum_with_steps(binary_data, word_size):
    while len(binary_data) % word_size != 0:
        binary_data = '0' + binary_data

    steps = []
    final_sum = '0' * word_size

    for i in range(0, len(binary_data), word_size):
        word = binary_data[i:i + word_size]
        prev_sum = final_sum
        final_sum, carry_steps = binary_addition_with_steps(final_sum, word)

        steps.append({
            "word": word,
            "previous_sum": prev_sum,
            "result_sum": final_sum
        })

    checksum = ''.join('1' if bit == '0' else '0' for bit in final_sum)

    return final_sum, checksum, steps


# 🔴 LAB RULE
def validate_data(checksum):
    return all(bit == '0' for bit in checksum)


# ================= DJANGO VIEW =================

def checksum_view(request):
    context = {}

    if request.method == "POST":
        data_input = request.POST.get("binary_data", "").strip()
        word_size = int(request.POST.get("word_size", 4))

        if not data_input or not all(bit in "01 " for bit in data_input):
            context["error"] = "Enter valid binary data (0s and 1s only)."
            return render(request, "checksum.html", context)

        binary_data = data_input.replace(" ", "")

        final_sum, checksum, steps = calculate_checksum_with_steps(binary_data, word_size)
        encoded_data = data_input + " " + checksum

        context.update({
            "input_data": data_input,
            "final_sum": final_sum,
            "checksum": checksum,
            "encoded_data": encoded_data,
            "status": "Error Free ✅" if validate_data(checksum) else "Error Detected ❌",
            "steps": steps
        })

    return render(request, "checksum.html", context)
