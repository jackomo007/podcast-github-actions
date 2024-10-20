import yaml
import xml.etree.ElementTree as xlm_tree

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    rss_element = xlm_tree.Element('rss', {'version':'2.0',
    'xmls:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmls:content': 'http://purl.org/rss/1.0/modules/content/'})

channel_element = xlm_tree.SubElement(rss_element, 'channel')
link_prefix = yaml_data['link']

xlm_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xlm_tree.SubElement(channel_element, 'format').text = yaml_data['format']
xlm_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
xlm_tree.SubElement(channel_element, 'itunes:author').text = yaml_data['author']
xlm_tree.SubElement(channel_element, 'description').text = yaml_data['description']
xlm_tree.SubElement(channel_element, 'itunes:image', {'href': link_prefix + yaml_data['image']})
xlm_tree.SubElement(channel_element, 'language').text = yaml_data['language']
xlm_tree.SubElement(channel_element, 'link').text = link_prefix

xlm_tree.SubElement(channel_element, 'itunes:category', {'text': yaml_data['category']})

for item in yaml_data['item']:
    item_element = xlm_tree.SubElement(channel_element, 'item')
    xlm_tree.SubElement(item_element, 'title').text = item['title']
    xlm_tree.SubElement(item_element, 'itunes:author').text = yaml_data['author']
    xlm_tree.SubElement(item_element, 'description').text = item['description']
    xlm_tree.SubElement(item_element, 'itunes:duration').text = item['duration']
    xlm_tree.SubElement(item_element, 'pubDate').text = item['published']
    xlm_tree.SubElement(item_element, 'title').text = item['title']
    
    enclosure = xlm_tree.SubElement(item_element, 'enclosure', {
        'url': link_prefix + item['file'],
        'type': 'audio/mpeg',
        'length': item['length']
    })

output_tree = xlm_tree.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)