# JU24-StructureSense-AI
GEN AI

"StructureSense AI: Extracting Structured Data from Unstructured Documents Without Relying Only on Bounding Boxes"

✅ Problem Statement
Many document extraction tools (especially for PDFs and scanned files) rely heavily on bounding boxes to extract layout-based data (text, tables, images). But this fails when:

Documents are digitally generated, not scanned (no bounding boxes).

Logical sections are spread across pages.

Semantic structure is more important than visual layout (e.g., policies, reports, SOPs).

🎯 Objective
Build an AI system that:

Extracts structured data (titles, paragraphs, tables, images) from documents (PDFs, DOCX, scanned images).

Detects semantic patterns like:

Section headers (Executive Summary, Financial Table, etc.)

Table structures (based on lines, keywords, or spacing)

Inline vs block content

Outputs structured JSON with labeled content (sections, tables, images).

Does not rely only on bounding boxes (uses NLP, layout inference, heuristics).

📁 Output Format (JSON)
json
Copy
Edit
{
  "document_title": "Q2 2025 – Company Performance Report",
  "sections": [
    {
      "title": "Executive Summary",
      "content_type": "text",
      "text": "Our company achieved strong growth in Q2 2025..."
    },
    {
      "title": "Financial Overview",
      "content_type": "table",
      "table": [
        ["Metric", "Q1 2025", "Q2 2025", "Change (%)"],
        ["Revenue", "$2,000,000", "$2,400,000", "+20%"],
        ...
      ]
    },
    {
      "title": "Key Visuals",
      "content_type": "image",
      "image_path": "output/images/figure_1.png"
    }
  ]
}
🛠 Tech Stack
Task	Tool/Library
PDF parsing	pdfplumber, PyMuPDF
DOCX parsing	python-docx
Image extraction	PyMuPDF, pdf2image
Table detection	camelot, pdfplumber, or layout-aware parsing
Text classification / NLP	spaCy, transformers, regex, LLM if needed
Output	JSON structured schema
UI	Streamlit

📦 Folder Structure
bash
Copy
Edit
structure-sense-ai/
├── app.py                   # Streamlit UI
├── utils/
│   ├── extract_text.py      # Extracts section-wise text
│   ├── extract_tables.py    # Detects and extracts tables
│   ├── extract_images.py    # Extracts figures/images
│   └── semantic_parser.py   # Analyzes patterns without bounding boxes
├── samples/
│   └── sample_q2_report.pdf # Sample document
└── output/
    ├── structured.json
    └── images/
🔍 Key Insight
You can detect structure from unstructured docs using:

Section Title Patterns (e.g., uppercase, bold, line spacing)

Semantic cues (e.g., "Summary", "Table", "Conclusion")

Natural language structure (NLP: Named Entity, Dependency Parsing)

Heuristics — based on layout + content mix

Bounding boxes help, but semantic + positional logic works for born-digital PDFs and DOCX files.
