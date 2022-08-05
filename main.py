import csv
data = []
findHiddenLikes = False
credentials = "igor_metrica"
import time

def getLikes(posts):

  global findHiddenLikes
  likes = 0
  count = 30
  likers = []
  
  try:
    
    for index, post in enumerate(posts, 1):
      
      if findHiddenLikes:

        if count != 0:

          if post.likes < 4:
  
            print("    - Hidden Likes")
            likers = post.get_likes()
  
            try:
              for iteration, item in enumerate(likers):
                likes+=1
                print(item.username)
                time.sleep(.25)
              print("        - Current Likes: ", likes)
            
            except:
              pass

            time.sleep(30)
            
          else:
            likes += post.likes
            
          count -= 1
        
        else:
          break
          break
          
      else: # don't find hidden likes

        if not findHiddenLikes:

          if count != 0:
  
            if post.likes < 4:
              likes += 0
              
            else:
              likes += post.likes
              
            count -= 1
          
          else:
            break
            break
    
  except:
    pass
    
  return likes

def getComments(posts):

  comments = 0
  count = 30
  
  try:
    for index, post in enumerate(posts, 1):
      if count != 0:
        comments += post.comments
        count -= 1
      else:
        break
        break
  except:
    exit()

  return comments

def getData(username):

  global credentials

  import instaloader
  bot = instaloader.Instaloader()

  bot.load_session_from_file(credentials)
  
  # bot.download_profile(Username, profile_pic_only = True)
  
  profile = instaloader.Profile.from_username(bot.context, username)
  
  username = profile.username
  print("    - Username: ", username)
  
  followers = profile.followers
  print("    - Followers: ", followers)
  
  posts = profile.get_posts()
  likes = getLikes(posts)
  print("    - Likes: ", likes)
  
  posts = profile.get_posts()
  comments = getComments(posts)
  print("    - Comments: ", comments)

  userMetrics = [username, followers, likes, comments]

  data.append(userMetrics)

def toCsv(data):

  # Open or create a CSV file, with "w" or write permission
  f = open("data.csv", "w")

  # initialize the writer
  writer = csv.writer(f)

  # write the header
  writer.writerow(["Username", "Followers", "Likes", "Comments"])

  for player in data:
    writer.writerow(player)
  f.close()

  print("    - ✅ Data written to csv file ")

def main():

  usernames = []
    
  # Using readlines()
  file1 = open('players.txt', 'r')
  Lines = file1.readlines()

  # Strips the newline character
  for line in Lines:
    line = line.replace("@","")
    line = line.replace('\n', '')
    usernames.append(line)

  for username in usernames:

    print("🔍 Evaluating ", username)
    getData(username)
    toCsv(data)

main()
