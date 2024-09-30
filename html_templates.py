import os
css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

def get_bot_template(MSG):

    bot_template = f'''
    <div class="chat-message bot">
        <div class="avatar">
            <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
        </div>
        <div class="message">{MSG}</div>
    </div>
    '''
    return bot_template

def get_user_template(MSG):
    if os.path.exists("image.txt"):
        with open("image.txt", "r") as f:
            img_src = f.read()
    else:
        img_src = "https://img.freepik.com/free-vector/user-blue-gradient_78370-4692.jpg?t=st=1727709499~exp=1727713099~hmac=a256c9af8f5c3c8286cfe84fcaabf59c7731cdb6b8c4d6e33aba3b36a354f26f&w=740"
        
    user_template = f'''
    <div class="chat-message user">
        <div class="avatar">
            <img src="{img_src}" width="350" alt="Grab Vector Graphic Person Icon | imagebasket" /></a>
        </div>    
        <div class="message">{MSG}</div>
    </div>
    '''
    return user_template


