import locale
def calculate_tax(income, num_children, num_elderly):
    # 定义税率和速算扣除数
    tax_rate = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
    quick_deduction = [0, 210, 1410, 2660, 4410, 7160, 15160]
    tax_bracket = [3000, 12000, 25000, 35000, 55000, 80000, 100000, 150000]

    # 免税额
    tax_free = 5000
    # 五险一金
    insurance = 0
    # 子女教育每月扣除1000元
    children_deduction = num_children * 1000
    # 赡养老人每月扣除2000元
    elderly_deduction = num_elderly * 2000
    # 计算应纳税所得额
    taxable_income = income - tax_free - insurance - children_deduction - elderly_deduction

    # 计算税额
    for i in range(len(tax_rate)):
        if taxable_income <= tax_bracket[i]:
            tax = taxable_income * tax_rate[i] - quick_deduction[i]
            break
    else:
        tax = taxable_income * tax_rate[-1] - quick_deduction[-1]

    return max(0, tax)

def formatCurrency(money):
    return locale.currency(money, grouping=True)

locale.setlocale(locale.LC_ALL, '')

# 计算养育两个子女，赡养 1 位老人的情况下的税额
incoming = 50000
tax = calculate_tax(incoming, 2, 1)
print(f"{formatCurrency(incoming)} 应缴纳的税额是：{formatCurrency(tax)}元，占比：{tax / incoming:.2%}")

incoming = 150000
tax = calculate_tax(incoming, 2, 1)
print(f"{formatCurrency(incoming)} 应缴纳的税额是：{formatCurrency(tax)}元，占比：{tax / incoming:.2%}")
