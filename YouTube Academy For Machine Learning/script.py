import pandas as pd
import json
from pprint import pprint


def get_topic_data(df):
    df_temp = df[['TITLE', 'URL', 'Instructor', 'Interview Questions']]

    def get_embed_url(in_url):
        if "youtube.com" in in_url and '/playlist?' not in in_url:
            in_url = in_url.replace('watch?v=', 'embed/')
        elif "youtu.be" in in_url and '/playlist?' not in in_url:
            in_url = in_url.replace('youtu.be/', 'youtube.com/embed/')
        else :
            in_url = 'NA'

        return in_url

    df_temp['embed_url'] = df_temp['URL'].apply(get_embed_url)
    # print(df_temp)

    df_temp_dict = df_temp.to_dict(orient='records')
    data = []
    for d in df_temp_dict:
        # print(d['Interview Questions'])
        if d['Interview Questions'] != 'Not Applicable':
            interview_questions = f"<a href='{d['Interview Questions']}' target='_blank'>Interview Questions</a>"
        else:
            interview_questions = 'NA'

        if d['embed_url'] != 'NA':
            embed_code = f"""<iframe class="custom_iframe" height="310" src="{d['embed_url']}" title="{d['TITLE']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>"""
        else:
            embed_code = "NA"

        data.append({
            "TITLE": f"<a href='{d['URL']}' target='_blank'>{d['TITLE']}</a>",
            "INSTRUCTOR": d['Instructor'],
            "INTERVIEW_QUES": interview_questions,
            "EMBED_CODE": embed_code
        })
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

    # pprint(data)
    return data

df = pd.read_excel('input.xlsx', sheet_name='Machine Learning')

unique_topics = df['TOPIC'].unique().tolist()

# print(unique_topics)

all_topic_data = {}
for topic in unique_topics:
    df_temp = df[df['TOPIC'] == topic]
    all_topic_data[topic] = get_topic_data(df_temp)

# pprint(all_topic_data)


with open("input.html", "r") as f:
    html_content = f.read()


def get_html_li(title, instructor, interview_questions, embed_code):
    html_template_for_video_section = f"""
<li class="customli">
    <div>{title}</div>
    <div>{instructor}</div>
    <div>{interview_questions}</div>
    <div>{embed_code}</div>
</li>
"""
    return html_template_for_video_section

script = """"""

def get_script_for_topic(cn, id):
    script_template = """$('h2.{}').click(function () {{
            $("div#{}").fadeToggle();
            $("h2.{} > .arrow").toggleClass('up').toggleClass('down');
        }}); \n"""
    return script_template.format(cn, id, cn)

for topic in all_topic_data:
    topic_classname = ''.join(e for e in topic if e.isalpha())

    html_content += f"\n<h2 class='custom{topic_classname}Header'> <span class='arrow up'></span> {topic}</h2>\n<div id='custom{topic_classname}'><ol>\n"
    for video in all_topic_data[topic]:
        html_content += get_html_li(video['TITLE'], video['INSTRUCTOR'], "" if video['INTERVIEW_QUES'] == "NA" else video['INTERVIEW_QUES'], "" if video['EMBED_CODE'] == "NA" else video['EMBED_CODE'])
    html_content += "\n</ol>\n</div>\n"
    script += get_script_for_topic(f"custom{topic_classname}Header", f"custom{topic_classname}")

html_content += "\n<span style='opacity:0;'>Tags: Machine Learning,Technology,Video,YouTube Academy,</span>"

html_content += "\n<script>\n" + script + """\n $(".customLink.toggleBtn").click(function () {
        $("h2[class$='Header']").click();
    });\n</script>"""

with open("output.html", "w") as f:
    f.write(html_content)