from bisheng_unstructured.documents.pdf_parser.pdf import PDFDocument
from bisheng_unstructured.documents.html_utils import visualize_html, save_to_txt

TEST_RT_URL = 'http://192.168.106.12:9001/v2.1/models/'


def test_pdf_doc():
  url = TEST_RT_URL
  layout_ep = url + 'elem_layout_v1/infer'
  cell_model_ep = url + 'elem_table_cell_detect_v1/infer'
  rowcol_model_ep = url + 'elem_table_rowcol_detect_v1/infer'
  table_model_ep = url + 'elem_table_detect_v1/infer'

  model_params = {
    'layout_ep': layout_ep,
    'cell_model_ep': cell_model_ep,
    'rowcol_model_ep': rowcol_model_ep,
    'table_model_ep': table_model_ep,
  }

  filename = "examples/docs/layout-parser-paper-fast.pdf"
  pdf_doc = PDFDocument(
    file=filename, 
    model_params=model_params,
    n=2)
  pages = pdf_doc.pages
  elements = pdf_doc.elements

  visualize_html(elements, 'data/layout-parser-paper-fast-v2.html')
  save_to_txt(elements, 'data/layout-parser-paper-fast-v2.txt')


def test_pdf_doc2():
  url = TEST_RT_URL
  layout_ep = url + 'elem_layout_v1/infer'
  cell_model_ep = url + 'elem_table_cell_detect_v1/infer'
  rowcol_model_ep = url + 'elem_table_rowcol_detect_v1/infer'
  table_model_ep = url + 'elem_table_detect_v1/infer'

  model_params = {
    'layout_ep': layout_ep,
    'cell_model_ep': cell_model_ep,
    'rowcol_model_ep': rowcol_model_ep,
    'table_model_ep': table_model_ep,
  }

  filename = "examples/docs/layout-parser-paper.pdf"
  pdf_doc = PDFDocument(
    file=filename, 
    model_params=model_params,
    start=0)
  pages = pdf_doc.pages
  elements = pdf_doc.elements
  visualize_html(elements, 'data/layout-parser-paper-v2.html')
  save_to_txt(elements, 'data/layout-parser-paper-v2.txt')


def test_pdf_doc3():
  url = TEST_RT_URL
  layout_ep = url + 'elem_layout_v1/infer'
  cell_model_ep = url + 'elem_table_cell_detect_v1/infer'
  rowcol_model_ep = url + 'elem_table_rowcol_detect_v1/infer'
  table_model_ep = url + 'elem_table_detect_v1/infer'

  model_params = {
    'layout_ep': layout_ep,
    'cell_model_ep': cell_model_ep,
    'rowcol_model_ep': rowcol_model_ep,
    'table_model_ep': table_model_ep,
  }

  filename = "examples/docs/sw-flp-1965-v1.pdf"
  pdf_doc = PDFDocument(
    file=filename, 
    model_params=model_params,
    start=0,
    n=5)
  pages = pdf_doc.pages
  elements = pdf_doc.elements
  # visualize_html(elements, 'data/sw-flp-1965-v1.html')
  # save_to_txt(elements, 'data/sw-flp-1965-v1.txt')


def test_pdf_doc4():
  url = TEST_RT_URL
  layout_ep = url + 'elem_layout_v1/infer'
  cell_model_ep = url + 'elem_table_cell_detect_v1/infer'
  rowcol_model_ep = url + 'elem_table_rowcol_detect_v1/infer'
  table_model_ep = url + 'elem_table_detect_v1/infer'

  model_params = {
    'layout_ep': layout_ep,
    'cell_model_ep': cell_model_ep,
    'rowcol_model_ep': rowcol_model_ep,
    'table_model_ep': table_model_ep,
  }

  filename = "examples/docs/sw-flp-1965-v1.pdf"
  pdf_doc = PDFDocument(
    file=filename, 
    model_params=model_params,
    enhance_table=False,
    start=0)
  pages = pdf_doc.pages
  elements = pdf_doc.elements
  visualize_html(elements, 'data/sw-flp-1965-v1.1.html')
  save_to_txt(elements, 'data/sw-flp-1965-v1.1.txt')


def test_pdf_doc5():
  url = TEST_RT_URL
  layout_ep = url + 'elem_layout_v1/infer'
  cell_model_ep = url + 'elem_table_cell_detect_v1/infer'
  rowcol_model_ep = url + 'elem_table_rowcol_detect_v1/infer'
  table_model_ep = url + 'elem_table_detect_v1/infer'

  model_params = {
    'layout_ep': layout_ep,
    'cell_model_ep': cell_model_ep,
    'rowcol_model_ep': rowcol_model_ep,
    'table_model_ep': table_model_ep,
  }

  filename = "examples/docs/layout-parser-paper.pdf"
  pdf_doc = PDFDocument(
    file=filename, 
    model_params=model_params,
    start=0)
  pages = pdf_doc.pages
  elements = pdf_doc.elements
  visualize_html(elements, 'data/layout-parser-paper-v1.1.html')
  save_to_txt(elements, 'data/layout-parser-paper-v1.1.txt')


def test_pdf_doc6():
  url = TEST_RT_URL
  layout_ep = url + 'elem_layout_v1/infer'
  cell_model_ep = url + 'elem_table_cell_detect_v1/infer'
  rowcol_model_ep = url + 'elem_table_rowcol_detect_v1/infer'
  table_model_ep = url + 'elem_table_detect_v1/infer'

  model_params = {
    'layout_ep': layout_ep,
    'cell_model_ep': cell_model_ep,
    'rowcol_model_ep': rowcol_model_ep,
    'table_model_ep': table_model_ep,
  }

  filename = "examples/docs/达梦数据库招股说明书.pdf"
  pdf_doc = PDFDocument(
    file=filename, 
    model_params=model_params,
    start=0, n=10)
  pages = pdf_doc.pages
  elements = pdf_doc.elements
  visualize_html(elements, 'data/达梦数据库招股说明书-v1_1.html')
  save_to_txt(elements, 'data/达梦数据库招股说明书-v1_1.txt')



def test_pdf_doc7():
  url = TEST_RT_URL
  layout_ep = url + 'elem_layout_v1/infer'
  cell_model_ep = url + 'elem_table_cell_detect_v1/infer'
  rowcol_model_ep = url + 'elem_table_rowcol_detect_v1/infer'
  table_model_ep = url + 'elem_table_detect_v1/infer'

  model_params = {
    'layout_ep': layout_ep,
    'cell_model_ep': cell_model_ep,
    'rowcol_model_ep': rowcol_model_ep,
    'table_model_ep': table_model_ep,
  }

  filename = "examples/docs/maoxuan_scan.pdf"
  pdf_doc = PDFDocument(
    file=filename, 
    model_params=model_params,
    enhance_table=False,
    start=0, n=100)
  pages = pdf_doc.pages
  elements = pdf_doc.elements
  visualize_html(elements, 'data/maoxuan_scan-v1_1.html')
  save_to_txt(elements, 'data/maoxuan_scan-v1_1.txt')


# test_pdf_doc()
# test_pdf_doc2()
# test_pdf_doc3()
# test_pdf_doc4()
# test_pdf_doc5()
# test_pdf_doc6()
test_pdf_doc7()