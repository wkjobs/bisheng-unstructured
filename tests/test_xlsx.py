from bisheng_unstructured.documents.html_utils import save_to_txt, visualize_html
from bisheng_unstructured.partition.xlsx import partition_xlsx


def test1():
    filename = "./examples/docs/test.xlsx"
    elements = partition_xlsx(filename=filename)

    output_file = "./data/test_v1.0.html"
    output_file2 = "./data/test_v1.0.txt"
    visualize_html(elements, output_file)
    save_to_txt(elements, output_file2)


test1()
