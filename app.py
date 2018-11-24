from flask import *
import json, math

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
	json_news_data = open("data/news.json")
	news_data = json.load(json_news_data)
	json_news_data.close()

	news_item = news_data[0]
	return render_template("index.html", bgimage=True, news_item=news_item)

@app.route("/repertoire")
def repertoire():
	json_song_data = open("data/songs.json")
	song_data = json.load(json_song_data)
	json_song_data.close()
 	return render_template("repertoire.html", semesters=song_data)

@app.route("/current_members")
def current_members():
	json_current_members_data = open("data/current_members.json")
	current_members_data = json.load(json_current_members_data)
	json_current_members_data.close()

	json_leadership_data = open("data/leadership.json")
	leadership_data = json.load(json_leadership_data)
	json_leadership_data.close()

	return render_template("current_members.html", current_members=current_members_data, leadership=leadership_data)

@app.route("/alumni")
def alumni():
	json_alumni_data = open("data/alumni.json")
	alumni_data = json.load(json_alumni_data)
	json_alumni_data.close()
	return render_template("alumni.html", alumni=alumni_data)

@app.route("/news")
def news():
	num_items_per_page = 4

	json_news_data = open("data/news.json")
	news_data = json.load(json_news_data)
	json_news_data.close()

	cur_page = int(request.args.get('page', 1))
	tot_num_pages = int( math.ceil( (len(news_data)+0.0)/num_items_per_page ))
	other_pages_to_show = range( max(1, cur_page-2), min(tot_num_pages, cur_page+2) )

	if (cur_page-1) < 3:
		other_pages_to_show = range(1, min(tot_num_pages+1, 6))
	elif (tot_num_pages-cur_page) < 3:
		other_pages_to_show = range( max(1, tot_num_pages-4), tot_num_pages+1)
	else:
		other_pages_to_show = range( max(1, cur_page-2), min(tot_num_pages+1, cur_page+3) )

	news_items = news_data[ (cur_page-1)*num_items_per_page : cur_page*num_items_per_page ]
	return render_template("news.html", news_items=news_items, cur_page=cur_page,
	                       tot_num_pages=tot_num_pages, other_pages_to_show=other_pages_to_show)

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/merch")
def merch():
	return render_template("merch.html")

#@app.route("/media")
#def media():
#	return render_template("media.html")

if __name__ == "__main__":
    app.run()
