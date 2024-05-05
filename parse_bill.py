from lxml import etree
import xml.etree.ElementTree as ET
import json

def parse_bill(xml_string):
    # Read the HTML file
    tree = ET.fromstring(xml_string)
    ns = {'dc': 'http://purl.org/dc/elements/1.1/'}
    data = {
        "title": tree.find('.//dc:title', namespaces=ns).text,
        "sections": []
    }

        # Loop through each section in the XML
    sections = tree.findall('.//section')
    for section in sections:
        section_id = section.get('id')
        section_title = section.find('.//header').text if section.find('.//header') is not None else "No Title"

        # Collect all text within the section by iterating through each element
        section_texts = []
        for elem in section.iter():
            if elem.text:
                section_texts.append(elem.text.strip())
        
        # Combine all texts within a section, replacing newline characters
        section_content = ' '.join([text.replace('\n', ' ').strip() for text in section_texts if text])

        # Append the structured section to the data dictionary
        data['sections'].append({
            "section_id": section_id,
            "title": section_title,
            "content": section_content
        })

    # Write the structured data to a JSON file
    with open('bill_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    return data

# Example usage
# xml_file = './output.xml'
# parse_bill(xml_file)
# print(json_data)