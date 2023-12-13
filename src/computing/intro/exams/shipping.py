order_total = 30
coupon_value = 3
coupon_valid = True

# Imagine you are writing the code for an online shopping
# platform. On this platform, a $5 shipping fee is added unless
# the order total is over $50; if the original order total is $50
# or higher (before subtracting coupons), shipping is free.
#
# Additionally, buyers may have coupons. If the coupon is valid,
# the price is subtracted from the order.
#
# The order total, coupon value, and coupon validity are
# reflected above as order_total, coupon_value, and coupon_valid.
# Based on these, calculate the total for an order, and print the
# sentence:
#
# Your total is: $32
#
# 32 would be replaced by the actual value based on the values
# of order_total, coupon_value, and coupon_valid.
#
# HINT: You may use conditionals on this problem, but you don't
# need to. Remember, you can use boolean statements in mathematical
# calculations. Multiplying by False is the same as multiplying
# by 0; multiplying by True is the same as multiplying by 1.


# Add your code here!

if order_total < 50:
    order_total += 5

if coupon_valid:
    order_total -= coupon_value

print(f"Your total is: ${order_total}")
