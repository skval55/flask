from flask import Flask, request, render_template
import stories

app = Flask(__name__)

story = stories.story

@app.route('/')
def get_prompts():
    """get prompts for madlib game from user"""
    words = story.prompts
    return render_template("madlibs.html", words=words)

@app.route('/story')
def make_story():
    """generates a story using the words entered by user"""
    # ans = {}
    # for word in story.prompts:
    #     ans[word] = request.args[word]

    ans = story.generate(request.args)
  
    return render_template('story.html', story=ans)

 