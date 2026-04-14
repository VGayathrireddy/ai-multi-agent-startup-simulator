from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def format_business_plan(data: dict) -> str:
    return f"""
================ BUSINESS PLAN ================

1. Executive Summary
{data['refined_idea']}

---------------------------------------------

2. Product & Problem
{data['idea_full']}

---------------------------------------------

3. Market Analysis
{data['market']}

---------------------------------------------

4. Business Model
{data['business']}

---------------------------------------------

5. Marketing Strategy
{data['marketing']}

---------------------------------------------

=============================================
"""

def save_to_docx(data: dict):
    doc = Document()

    # ✅ Set margins (narrow)
    section = doc.sections[0]
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)

    # ✅ Title
    title = doc.add_paragraph()
    title_run = title.add_run("BUSINESS PLAN")
    title_run.bold = True
    title_run.font.name = "Times New Roman"
    title_run.font.size = Pt(18)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph("\n")

    # 🧩 Helper function
    def add_section(heading, content):
        # Heading
        h = doc.add_paragraph()
        run = h.add_run(heading)
        run.bold = True
        run.font.name = "Times New Roman"
        run.font.size = Pt(16)

        # Content
        for line in content.split("\n"):
            p = doc.add_paragraph()
            run = p.add_run(line)
            run.font.name = "Times New Roman"
            run.font.size = Pt(14)

    # ✅ Sections
    add_section("1. Executive Summary", data["refined_idea"])
    add_section("2. Product & Problem", data["idea_full"])
    add_section("3. Market Analysis", data["market"])
    add_section("4. Business Model", data["business"])
    add_section("5. Marketing Strategy", data["marketing"])

    # 💾 Save
    doc.save("business_plan.docx")