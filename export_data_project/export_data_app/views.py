from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64

lst = [
    [2821.99, 3430.59, 4518.54], [549.45, 614.9, 794.07], [
        393.65, 310.44, 370.74], [242.88, 208.77, 164.32],
    [57.87, 107.6, 124.0], [35.74, 21.89, 91.15], [
        29.76, 23.78, 35.23], [29.75, 73.98, 25.83], [9.21, 13.4, 15.36],
    [10.78, 11.29, 10.61], [1.03, 1.34, 7.24], [
        271.84, 327.45, 378.49], [2298.47, 2302.16, 2543.42],
    [740.3, 1178.76, 1413.06], [516.67, 688.76, 470.14], [
        106.38, 115.6, 167.67], [453.58, 406.16, 167.34],
    [53.65, 62.39, 84.43], [137.78, 215.19, 534.72], [
        29849.73, 26415.99, 38523.54], [35476.6, 45652.36, 51088.69],
    [4037.63, 15840.31, 11826.89], [4675.64, 7615.46, 8987.1], [
        435.80129999999997, 1585.0998000000002, 0.6295000000000001],
    [1651.83, 1487.33, 1761.12]
]

product = [
    "Onions", "Potatoes", "Green Chillies", "Tomatoes", "Shallots", "Garlics", "Lady Finger", "Walnuts", "Turmeric",
    "Pumpkin", "Peas", "Mangoes", "Grapes", "Bananas", "Pomegranates", "Apples", "Oranges", "Water Melon",
    "Areca Nuts and Betel Leaves", "Basmati Rice", "Non-Basmati Rice", "Wheat", "Maize", "Millet", "Cucumber"
]

percentage = [
    [19.86, 18.78, 17.37, 10.0, 5.92, 28.07], [44.64, 11.74, 10.64,
                                               8.51, 5.97, 18.5], [71.85, 11.13, 4.76, 2.63, 2.08, 7.55],
    [52.4, 18.76, 8.4, 7.35, 7.04, 6.05], [32.73, 28.47, 11.23,
                                           7.6, 6.97, 13.0], [63.85, 10.6, 6.23, 4.94, 4.07, 10.31],
    [31.31, 18.25, 11.18, 8.23, 7.12, 23.91], [47.15, 21.29, 18.23,
                                               5.07, 3.02, 5.24], [23.7, 21.03, 20.77, 8.79, 6.71, 19.0],
    [40.72, 19.51, 15.08, 12.16, 4.05, 8.48], [44.2, 15.33, 12.29,
                                               11.88, 6.77, 9.53], [15.23, 8.9, 7.73, 5.69, 5.58, 56.87],
    [37.66, 9.56, 7.77, 7.65, 5.67, 31.69], [22.31, 22.19, 19.56,
                                             9.8, 7.84, 18.3], [42.42, 20.41, 6.62, 6.5, 3.27, 20.78],
    [49.23, 44.49, 5.12, 0.5, 0.13, 0.53], [82.71, 15.35, 1.45,
                                            0.33, 0.05, 0.11], [36.36, 30.45, 21.37, 7.15, 2.4, 2.27],
    [28.61, 18.11, 16.09, 15.82, 5.04, 16.33], [21.71, 20.35, 7.87,
                                                6.98, 6.42, 36.67], [8.35, 7.63, 6.79, 6.64, 5.2, 65.39],
    [27.67, 18.59, 10.13, 9.93, 5.6, 28.08], [49.21, 25.09, 10.72,
                                              5.12, 3.97, 5.89], [17.89, 10.52, 9.44, 3.73, 4.67, 53.75],
    [28.52, 8.94, 8.78, 6.16, 5.54, 42.06]
]

country = [
    ['Bangladesh Pr', 'Malaysia', 'U Arab Emts',
        'Sri Lanka Dsr', 'Nepal', 'Others'],
    ['Nepal', 'Oman', 'Saudi Arab', 'Indonesia', 'Malaysia', 'Others'],
    ['U Arab Emts', 'Qatar', 'Oman', 'Kuwait', 'Bhutan', 'Others'],
    ['Bangladesh Pr', 'Nepal', 'Bhutan', 'Maldives', 'U Arab Emts', 'Others'],
    ['Malaysia', 'Sri Lanka Dsr', 'Singapore',
        'Thailand', 'U Arab Emts', 'Others'],
    ['Bangladesh Pr', 'Malaysia', 'U S A',
        'Vietnam Soc Rep', 'U Arab Emts', 'Others'],
    ['U K', 'Germany', 'U Arab Emts', 'Qatar', 'Singapore', 'Others'],
    ['U Arab Emts', 'Germany', 'U K', 'Netherland', 'New Zealand', 'Others'],
    ['U Arab Emts', 'Nepal', 'Indonesia', 'Bangladesh Pr', 'Algeria', 'Others'],
    ['U Arab Emts', 'Maldives', 'Qatar', 'Nepal', 'Bhutan', 'Others'],
    ['France', 'U S A', 'U Arab Emts', 'Bhutan', 'Egypt A Rp', 'Others'],
    ['U K', 'U S A', 'Qatar', 'Kuwait', 'Oman', 'Others'],
    ['Netherland', 'Bangladesh Pr', 'U Arab Emts', 'U K', 'Russia', 'Others'],
    ['Iran', 'Iraq', 'U Arab Emts', 'Oman', 'Uzbekistan', 'Others'],
    ['U Arab Emts', 'Bangladesh Pr', 'Nepal', 'Netherland', 'Qatar', 'Others'],
    ['Bangladesh Pr', 'Nepal', 'Bhutan', 'U Arab Emts', 'Saudi Arab', 'Others'],
    ['Bangladesh Pr', 'Nepal', 'Bhutan', 'U Arab Emts', 'Baharain Is', 'Others'],
    ['Nepal', 'U Arab Emts', 'Maldives', 'Bhutan', 'Qatar', 'Others'],
    ['Vietnam Soc Rep', 'U Arab Emts', 'Bangladesh Pr', 'Myanmar', 'Bhutan', 'Others'],
    ['Saudi Arab', 'Iran', 'Iraq', 'U Arab Emts', 'Yemen Republc', 'Others'],
    ['Benin', 'China P Rp', 'Senegal', 'Cote D Ivoire', 'Togo', 'Others'],
    ['Bangladesh Pr', 'Indonesia', 'Korea Rp',
        'U Arab Emts', 'Yemen Republc', 'Others'],
    ['Bangladesh Pr', 'Vietnam Soc Rep', 'Nepal',
        'Malaysia', 'Sri Lanka Dsr', 'Others'],
    ['U Arab Emts', 'Saudi Arab', 'Nepal', 'Bangladesh Pr', 'Japan', 'Others'],
    ['U S A', 'Russia', 'France', 'Spain', 'Germany', 'Others']
]


def product_graph(request, product_id):
    if 0 <= product_id < len(product):
        product_name = product[product_id]
        export_data = lst[product_id]

        # Create a bar chart
        plt.bar(['2020-21', '2021-22', '2022-23'], export_data)
        plt.xlabel('Year')
        plt.ylabel('Export Value')
        plt.title(f'Export Data for {product_name}')
        plt.tight_layout()

        # Save the plot to a BytesIO object
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()

        # Convert the BytesIO object to a base64 encoded string
        graph_data = base64.b64encode(buffer.getvalue()).decode()

        return render(request, 'export_data_app/product_graph.html', {'graph_data': graph_data, 'product_name': product_name})
    else:
        return render(request, 'export_data_app/product_not_found.html')


def product_pie_chart(request, product_id):
    if 0 <= product_id < len(product):
        product_name = product[product_id]
        export_data = percentage[product_id]

        # Create a pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(export_data, labels=country[product_id], autopct='%1.1f%%')
        plt.title(f'Export Data Distribution for {product_name}')
        plt.tight_layout()

        # Save the pie chart to a BytesIO object
        buffer = BytesIO()
        plt.savefig(buffer, format='jpeg')
        plt.close()

        # Convert the BytesIO object to a base64 encoded string
        pie_chart_data = base64.b64encode(buffer.getvalue()).decode()

        return render(request, 'export_data_app/product_graph.html', {'pie_data': pie_chart_data, 'product_name': product_name})
    else:
        return render(request, 'export_data_app/product_not_found.html')


def index(request):
    return render(request, 'export_data_app/index.html', {'products': product})


# ... (your data lists and other code)


def product_details(request, product_id):
    if 0 <= product_id < len(product):
        product_name = product[product_id]
        export_data_bar = lst[product_id]
        export_data_pie = percentage[product_id]

        # Create a bar chart
        plt.bar(['2020-21', '2021-22', '2022-23'], export_data_bar)
        plt.xlabel('Year')
        plt.ylabel('Export Value')
        plt.title(f'Export Data for {product_name}')
        plt.tight_layout()

        # Save the bar chart to a BytesIO object
        buffer_bar = BytesIO()
        plt.savefig(buffer_bar, format='png')
        plt.close()

        # Create a pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(export_data_pie, labels=country[product_id], autopct='%1.1f%%')
        plt.title(f'Export Data Distribution for {product_name}')
        plt.tight_layout()

        # Save the pie chart to a BytesIO object
        buffer_pie = BytesIO()
        plt.savefig(buffer_pie, format='png')
        plt.close()

        # Convert the BytesIO objects to base64 encoded strings
        bar_graph_data = base64.b64encode(buffer_bar.getvalue()).decode()
        pie_chart_data = base64.b64encode(buffer_pie.getvalue()).decode()

        return render(request, 'export_data_app/product_details.html', {
            'product_name': product_name,
            'bar_graph_data': bar_graph_data,
            'pie_chart_data': pie_chart_data
        })
    else:
        return render(request, 'export_data_app/product_not_found.html')
