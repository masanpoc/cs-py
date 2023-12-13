original_price = 15.0
num_shares = 100
final_price = 100.0

# Short selling is when an investor borrows some shares of a
# stock to sell at the current price, expecting that at a later
# date they can buy the stock at a lower price to give back.
# For example, if you anticipate the stock GME will drop in
# value, you might borrow 100 shares today, sell them for $15
# each, and expect to buy them back in two weeks for $10,
# netting you $500 in profit (100 * $15 - 100 * $10 = $500).
#
# A short squeeze occurs when instead of falling, the stock
# price rises. If instead of dropping to $10 per share, GME
# rose to, say, $100 per share, then the investor would owe
# $8500 (100 * $15 - 100 * $100 = -$8500).
#
# For this problem, let's only look at these short squeezes.
# original_price, num_shares, and final_price give the
# price at which an investor buys a stock, the number of
# shares they buy, and the price of the stock when they must
# buy their shares to return.
#
# Calculate the total amount lost by this attempt at short
# selling, and print it according to the following format:
#
# You lost: $8500.0
#
# You should round this number to two decimal places. To do
# this, you may use the round function. For example:
#
# rounded_num = round(123.456, 2)
#
# ...will result in rounded_num = 123.46. Do not worry about
# adding the extra 0 if the result is an even tenth ($8500.0
# is fine, you don't need to print $8500.00).


# Add your code here!

result = (original_price * num_shares - final_price * num_shares) * (-1)

print(f"You lost: ${round(result, 1)}")
