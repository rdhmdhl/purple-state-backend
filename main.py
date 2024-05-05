from parse_bill import parse_bill
from ask_groq import ask_groq
from get_bill import get_bill

def main():
    bill = get_bill()
    parsed_bill = parse_bill(bill)
    answer = ask_groq(parsed_bill)
    print(answer)

main()