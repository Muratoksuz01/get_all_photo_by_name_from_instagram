
import instaloader
profile_name = "your_username"
profile_pass="your_password"
l=instaloader.Instaloader()
l.login(profile_name,profile_pass)
l.download_profile("target_usernama",download_stories_only=False,profile_pic_only=False,profile_pic=True)#in here you can choosse whatever you want ,if you want ,make 'true' not 'false'
