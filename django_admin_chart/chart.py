def chart():
    fname = "./templates/duel_bar_chart.html"
    html_file = open(fname, 'r', encoding='utf-8')
    source_code = html_file.read()
    print(source_code)

