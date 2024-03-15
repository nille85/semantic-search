# Extracting PDFs
Learn more at: https://towardsdatascience.com/extracting-text-from-pdf-files-with-python-a-comprehensive-guide-9fc4003d517

import to also install poppler and tesseract
on Mac:

```brew install poppler```

```brew install tesseract```

How to use this:

```python

pdf_path = "input/report.pdf"
for dctkey, page_data in extract_text_from_pdf(pdf_path).items():
  page_content = page_data[-1]
  print(f"Page content for key '{dctkey}'")
  print("-----------------------------------")
  for content in page_content:
    print(f"{content}")
```