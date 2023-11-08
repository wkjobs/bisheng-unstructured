import os

from bisheng_unstructured.partition.common import convert_office_doc


class DocxToPDF(object):
    def __init__(self, kwargs={}):
        cmd_template = """
          pandoc -o {1} --pdf-engine=xelatex {0}
              -V mainfont="Alibaba PuHuiTi"
              -V sansfont="Alibaba PuHuiTi"
              -V monofont="Cascadia Mono"
              -V CJKmainfont="Alibaba PuHuiTi"
              -V CJKsansfont="Alibaba PuHuiTi"
              -V CJKmonofont="Cascadia Mono"
        """

        def _norm_cmd(cmd):
            return " ".join([p.strip() for p in cmd.strip().split()])

        self.cmd_template = _norm_cmd(cmd_template)

    def render(self, input_file, output_file=None, to_bytes=False):
        type_ext = input_file.rsplit(".", 1)[-1]
        filename = os.path.basename(input_file)
        temp_dir = os.path.dirname(input_file)

        assert type_ext in ["doc", "docx"]

        if output_file is None:
            output_filename = filename.rsplit(".", 1)[0] + ".pdf"
            output_file = os.path.join(temp_dir, output_filename)

        if type_ext == "doc":
            convert_office_doc(input_file, temp_dir)
            input_file = os.path.join(temp_dir, filename.rsplit(".", 1)[0] + ".docx")

        cmd = self.cmd_template.format(input_file, output_file)
        try:
            exit_code = os.system(cmd)
            if exit_code != 0:
                raise Exception("error in transforming doc to pdf")
        except Exception as e:
            raise e

        if to_bytes:
            return open(output_file, "rb").read()
