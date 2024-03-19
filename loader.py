from pdf_extractor import extract_text_from_pdf

# Display the content of the page
pdf_paths = ["input/report.pdf"]

def load_document(pdf_path):
    page_dictionary = extract_text_from_pdf(pdf_path)
    document = reconstruct_content(page_dictionary)
    return document

def reconstruct_content(page_dictionary):
    full_content = ""
    for dctkey, page_data in page_dictionary.items():
        # Access page content using the last element in the list
        page_content = page_data[-1]
        # Do something with the page content
        for content in page_content:
            full_content += content
    return full_content