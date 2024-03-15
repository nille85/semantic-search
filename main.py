from pdf_extraction import extract_text_from_pdf

# Display the content of the page
pdf_paths = ["input/report.pdf"]

for pdf_path in pdf_paths:
    for dctkey, page_data in extract_text_from_pdf(pdf_path).items():
        # Access page content using the last element in the list
        page_content = page_data[-1]
        # Do something with the page content
        print(f"[Source {pdf_path}, Page '{dctkey}']")
        print("-----------------------------------")
        block = 0
        for content in page_content:
            length = len(content)
            print(f"Source {pdf_path}, Page '{dctkey}', Block {block}, Length {length}")
            print(f"{content}")
            print("--------------------")
            block = block + 1