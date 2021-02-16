import textract
from pororo import Pororo


class PdfSummarizer:
    def __init__(self, pdf_dir):
        self.mt = Pororo(task="translation", lang="multi")
        self.summarizer = Pororo(task='summary', model='extractive', lang='ko')

        self.txt = self.pdf2text(pdf_dir)
        self.trans = self.text_translation(self.txt, source='en', target='ko')
        self.sum = self.summarize(self.trans, gap=30)

        return self.sum

    def pdf2text(self, pdf_dir):
        txt = textract.process(pdf_name, method='pdfminer')
        txt_new = str(text)
        txt_new = txt_new.replace("\\n", " ")
        txt_new = txt_new.replace('\\x', '')
        return txt_new

    def text_translation(self, txt_in, source='en', target='ko'):
        trans = self.mt(txt_in, src=source, tgt=target)
        return trans

    def summarize(self, src, gap=10):
        parsed = src.split('.')

        sum_ = []
        for i in range(0, len(parsed), step=gap):
            sum_.append(self.summarizer('. '.join(parsed[i:i+gap])))
        sum__ = '\\n'.join(sum_)
        return sum__




def pdf2text(pdf_dir):
    txt = textract.process(pdf_name, method='pdfminer')
    txt_new = str(text)
    txt_new = txt_new.replace("\\n", " ")
    txt_new = txt_new.replace('\\x', '')

    return txt_new


def text_translation(txt_in, source='en', target='ko'):
    trans = mt(txt_in, src=source, tgt=target)



pdf_name = 'simclr.pdf'
text = textract.process(pdf_name, method='pdfminer')

text_new = str(text)
text_new = text_new.replace("\\n", " ")
text_new = text_new.replace('\\x', '')
