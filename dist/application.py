from cs50 import SQL
from flask import Flask, json, render_template, request, jsonify

app = Flask(__name__)

db = SQL('sqlite:///database.db')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
# <option value="default" selected>default</option>
#                         <option value="dracula">dracula</option>
#                         <option value="dark">dark</option>
#                         <option value="radical">radical</option>
#                         <option value="merko">merko</option>
#                         <option value="gruvbox">gruvbox</option>
#                         <option value="tokyonight">tokyonight</option>
#                         <option value="onedark">onedark</option>
#                         <option value="cobalt">cobalt</option>
#                         <option value="synthwave">synthwave</option>
#                         <option value="highcontrast">highcontrast</option>
    features_themes = [
        'dracula', 'dark', 'radical', 'merko', 'gruvbox', 'tokyonight', 'onedark', 'cobalt', 'synthwave', 'highcontrast' 
    ]

    features_color = [
        'brightgreen', 'green', 'yellow', 'yellowgreen', 'orange', 'red', 'grey', 'lightgrey', 'blueviolet'
    ]


    more_about_you = db.execute("SELECT * FROM about_you")
    
    social_medias = db.execute("SELECT * FROM social_medias")
    
    skills = db.execute('SELECT * FROM skills')

    return render_template('profile.html', more_about_you=more_about_you, social_medias=social_medias, skills=skills, themes=features_themes, colors=features_color)


@app.route('/submit', methods=['POST'])
def submit():
    markdown = ''

    # Greet Section
    name = request.form.get('name')
    if name != '':
        title = request.form.get('title')
        markdown += '# ' + title + ' ' + name + '\n'

    subtitle = request.form.get('subtitle')
    if subtitle != '':
        markdown += '### ' + subtitle + '\n'

    # More About You Section
    about_you_keys = request.form.getlist('more_about_you_key')
    about_you_values = request.form.getlist('more_about_you_value')
    about_you = {}
    for i in range(0, len(about_you_values)):
        if about_you_values[i] != '':
            about_you[about_you_keys[i]] = about_you_values[i]
    
    if len(about_you) != 0:
        markdown += '## About me\n'
        for key, value in about_you.items():
            markdown += key + ' ' + value + '\n\n'

    # Social Medias Section
    social_badges = db.execute("SELECT * FROM social_medias")

    markdown += '## Contact me:\n'

    gmail = request.form.get('gmail')
    if gmail != '':
        markdown += '[![Gmail Badge](' + social_badges[0]['link'] + ')](mailto:' + gmail + ')&nbsp;\n' 
        
    github = request.form.get('github username')
    if github != '':
        markdown += '[![Github Badge](' + social_badges[2]['link'] + ')](https://www.github.com/' + github + ')&nbsp;\n'

    twitch = request.form.get('twich')
    if twitch != '':
        markdown += '[![Twitch Badge](' + social_badges[4]['link'] + ')](https://www.twitch.tv/' + twitch + ')&nbsp;\n'

    linkedin = request.form.get('linkedin')
    if linkedin != '':
        markdown += '[![Linkedin Badge](' + social_badges[6]['link'] + ')](https://www.linkedin.com/in/' + linkedin + ')&nbsp;\n'

    instagram = request.form.get('instagram')
    if instagram != '':
        markdown += '[![Instagram Badge](' + social_badges[8]['link'] + ')](https://www.instagram.com/' + instagram + ')&nbsp;\n'

    devto = request.form.get('dev.to')
    if devto != '':
        markdown += '[![Dev.to Badge](' + social_badges[1]['link'] + ')](https://dev.to/' + devto + ')&nbsp;\n'

    tiktok = request.form.get('tiktok')
    if tiktok != '':
        markdown += '[![Tiktok Badge](' + social_badges[3]['link'] + ')](https://www.tiktok.com/' + tiktok + ')&nbsp;\n'

    medium = request.form.get('medium')
    if medium != '':
        markdown += '[![Medium Badge](' + social_badges[5]['link'] + ')](https://' + medium + '.medium.com/)&nbsp;\n'

    twitter = request.form.get('twitter')
    if twitter != '':
        markdown += '[![Twitter Badge](' + social_badges[7]['link'] + ')](https://twitter.com/' + twitch + ')&nbsp;\n'

    youtube = request.form.get('youtube')
    if youtube != '':
        markdown += '[![Youtube Badge](' + social_badges[9]['link'] + ')](https://www.youtube.com/channel/' + youtube + ')&nbsp;\n'
    
    # Skills Section
    skill_name = request.form.getlist('skill_name')
    
    if len(skill_name) > 0:
        markdown += '## My Skills\n'
        for skill in skill_name:
            markdown += '<img src="' + request.form.get(skill) + '" alt="' + skill + ' Badge" height="50" width="50">&nbsp;\n'

    # Cool Features Section
    
    # Github Status
    if request.form.get('gh_status_check') == 'true':
        markdown += '![GitHub stats](' + str(request.form.get('gh_status_url')) + ')\n'

    # Top Languages Card
    if request.form.get('gh_top_languages_check') == 'true':        
        markdown += '![Top Languages](' + str(request.form.get('top_languages_url')) + ')\n'

    # Profile Views
    if request.form.get('gh_views_check') == 'true':
        markdown += '![Profile Views](' + str(request.form.get('profile_views_url')) + ')\n'

    # Streak Stats
    if request.form.get('gh_streak_stats_check') == 'true':
        markdown += '![Streak Stats](' + str(request.form.get('streak_stats_url')) + ')\n'

    print(markdown)
    return markdown
