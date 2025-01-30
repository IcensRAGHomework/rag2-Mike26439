from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=1000,
        chunk_overlap=0,
        length_function=len,
        is_separator_regex=False,
    )
    split_documents = text_splitter.split_documents(documents)
    return split_documents[-1]

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    documents = loader.load()

    full_text = "\n".join(doc.page_content for doc in documents)

    recursive_text_splitter = RecursiveCharacterTextSplitter(
        separators=[r"\n.*第.{0,}章.{0,}?\n",  # 第x章
            r"第.{0,}\d{1,}.{0,}條.{0,}\n"  # 第 x 條
        ],
        is_separator_regex=True,
        chunk_size = 10,
        chunk_overlap = 0,
        length_function = len,
        add_start_index = False,
    )

    split_documents = recursive_text_splitter.split_text(full_text)
    return len(split_documents)

print(hw02_2(q2_pdf))