<template>
<div>
    <NavBar/>
    <div id="welcome" class="hero-acceuil">
        <div class="space"></div>

        <div class="page">
            <!-- cote gauche -->
            <div class="left-side">
                <div class="space-content"></div>
                <div class="content">
                    <h2>INSTALL PARTY IS HERE</h2>
                    <p>
                        Notre evenement phare est enfin là, au programme des conferences, panels, workshops et plein d'activités, vous pouvez en apprendre plus juste en bas!
                    </p>
                    <router-link to="Registration"><img src="../assets/welcome_screen/participer_button.png" class="participer-button"/></router-link>

                </div>
            </div>
            <div class="right-side">
                <img class="clubLogo" src="../assets/omc_logo_grey.png"/>
                <div class = "IPNameLogo sec1">
                    <img class="eventName"  src="../assets/install_party_new_era.png"/>
                    <img class="asset1"  src="../assets/welcome_screen/welcome_special_asset1.png"/>
                    <img class="IPlogo"  src="../assets/logoIP10.png"/>
                </div>

                    <ul class="IPNameLogo sec2 social-icons">
                        <li v-for="social_media in social_medias" :key="social_media.title">
                            <a :class="social_media.title" :href="social_media.url" target="_blank"><i :class="social_media.class_image"></i></a>
                        </li>
                    </ul>

            </div>
        </div>
        <ArrowDownWelcome title="En Savoir plus" color="gray"/>
    </div>
</div>
</template>

<script>
import NavBar from '../components/NavBar'
import ArrowDownWelcome from '../components/ArrowDownWelcome'
export default {
  name: "Acceuil",
  components: {
      NavBar,
      ArrowDownWelcome,
  },
  data: () => ({
      pics: [
          { title: "facebook", path: "/#/acceuil"},
          { title: "twitter", path: "/#/event"},
          { title: "gmail", path: "/#/planning"},
          { title: "instagram", path: "/#/sponsor"},
          { title: "youtube", path: "/#/apropos"},
      ],
      social_medias: [
          { title: "facebook", url: "https://www.facebook.com/openmindsclub/", class_image:'fab fa-facebook' },
          { title: "twitter", url: "https://twitter.com/clubopenminds", class_image:'fab fa-twitter'},
          { title: "linkedin", url: "https://www.linkedin.com/company/open-minds-club", class_image:'fab fa-linkedin'},
          { title: "instagram", url: "https://www.instagram.com/openmindsclub/", class_image:'fab fa-instagram'},
          { title: "youtube", url: "https://www.youtube.com/channel/UCTS5jQGSPHuuibdqLUqFAqw", class_image:'fab fa-youtube'},
      ],
      amount_scrolled: 0
  }),
  methods: {
    getImgUrl(pic){
        return  require('../assets/Social_Media_Logos/' + pic + ".png");
    },
    switchHome(){

    },
    handleWheel(event) {
        if(event.deltaY > 0){
            this.$router.push({ name: 'Home'})
        }
    }
  },

  mounted() {
      this.$el.addEventListener('wheel', this.handleWheel)
  },

  destroyed() {
      this.$el.removeEventListener('wheel', this.handleWheel)

  }
};
</script>


<style scoped >
.hero-acceuil {
    background-image: url("../assets/backgrounds/Index_background_3.jpg");
  /* Set a specific height */
  height: 100vh;
  width: 100%;
  /* Position and center the image to scale nicely on all screens */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}

.space{
    height: 8%;
}

.page{
    display: flex;
}

.left-side{
    flex: 5;
}

.space-content{
    height: 35%;
}

.content{
    margin-left: 20%;
    height: 50vh;
    text-align: center;
    overflow:hidden;
    text-overflow:ellipsis;
    word-wrap: break-word;
    overflow-y: scroll;
    -ms-overflow-style: none;  /* Hide scrollbar for IE and Edge */
    scrollbar-width: none; /* Hide scrollbar for Firefox */
}

/* Hide scrollbar for Chrome, Safari and Opera */
.content::-webkit-scrollbar {
  display: none;
}

.content h2{
    font-size: 2.9em;
    color: #4B535C;
    font-weight: bold;
    font-style: italic;
}

.content p{
    font-size: 1.9em;
    color: #4B535C;
}

.content .participer-button{
    margin-top: 5%;
    width: 40%;
}

.right-side {
    margin-left: 5%;
    margin-right: 10%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 70vh;
    flex: 7;
}

.clubLogo{
    width:16%;
}

.IPNameLogo{
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-around;
}

.sec1{
    width:95%;
    height: 40%;
    margin-top: 5%;
    margin-right: 10%;
    margin-left: 10%;
}

.sec2{
    width:70%;
    height: 10%;
    margin-top: 3%;
    margin-right: 30%;
    margin-left: 20%;
}

.eventName{
    width:60%;
    height:100%;
}

.IPlogo{
    width:30%;
    height:80%;
}

.asset1{
    width:5%;
    height:100%;
}


@media(max-width: 1300px) {
    .content h2{
        font-size: 2em;
    }

    .content p{
        font-size: 1.5em;
    }
}

@media(max-width: 850px) {
    .content h2{
        font-size: 25px;
    }

    .content p{
        font-size: 14px;
    }
}

@media (max-width: 1200px) and (max-aspect-ratio: 10/9)  {

    .hero-acceuil {
        background-image: url("../assets/backgrounds/white_shape.jpg");
        overflow-y: scroll;
        -ms-overflow-style: none;  /* Hide scrollbar for IE and Edge */
        scrollbar-width: none;
    }

    /* Hide scrollbar for Chrome, Safari and Opera */
    .hero-acceuil::-webkit-scrollbar {
      display: none;
    }

    .space{
        height: 0%;
    }

    .page{
        display: flex;
        flex-direction: column-reverse;
    }

    .content{
        margin-left: 5%;
        height: auto;
        overflow: auto;
        text-overflow: inherit;
        word-wrap: normal;
        overflow-y: auto;
    }

    .content h2{
        font-size: 30px;
    }

    .content p{
        font-size: 18px;
    }

    .right-side {
        margin-top: 10%;
        margin-left: 0%;
        margin-right: 0%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: auto;
        flex: auto;
    }

    .left-side{
        margin-top: 20%;
        flex: auto;
    }

    .asset1{
        width:5%;
        height:10vh;
    }

    .content .participer-button{
        margin-bottom: 10%;
    }

}

@media (max-width: 600px){
    .hero-acceuil {
        background-image: url("../assets/backgrounds/white_shape.jpg");
        overflow-y: scroll;
        -ms-overflow-style: none;  /* Hide scrollbar for IE and Edge */
        scrollbar-width: none;
    }

    /* Hide scrollbar for Chrome, Safari and Opera */
    .hero-acceuil::-webkit-scrollbar {
      display: none;
    }

    .space{
        height: 0%;
    }

    .page{
        display: flex;
        flex-direction: column-reverse;
    }

    .content{
        margin-left: 5%;
        height: auto;
        overflow: auto;
        text-overflow: inherit;
        word-wrap: normal;
        overflow-y: auto;
    }

    .content h2{
        font-size: 25px;
    }

    .content p{
        font-size: 15px;
    }

    .right-side {
        margin-top: 10%;
        margin-left: 0%;
        margin-right: 0%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: auto;
        flex: auto;
    }

    .left-side{
        margin-top: 10%;
        flex: auto;
    }

    .asset1{
        width:5%;
        height:10vh;
    }

    .content .participer-button{
        margin-bottom: 10%;
    }

}

@media(max-width: 500px) {

    .right-side {
        margin-left: 0%;
        margin-right: 0%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: auto;
        flex: 7;
    }

    .clubLogo{
        display:none;
    }

    .sec1{
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
        width:auto;
        height: auto;
        margin-top: 10%;
        margin-right: 10%;
        margin-left: 10%;
    }

    .sec2{
        margin-left: 30%;
    }

    .eventName{
        width:100%;
        height:auto;
        margin-bottom: 5%;
    }

    .IPlogo{
        width:50%;
        height:auto;
        margin-bottom: none;
    }

    .asset1{
        display: none;
    }

}

.social-icons{
    padding-left:0;
    width: 40%;
    margin-bottom:0;
    list-style:none
}

.social-icons li{
    display:inline-block;
    margin-bottom:4px
}

.social-icons li.title{
    margin-right:15px;
    text-transform:uppercase;
    color:#96a2b2;
    font-weight:700;
    font-size:13px
}

.social-icons a{
    background-color:#4B535C;
    color:#F2F5FE;
    font-size:16px;
    display:inline-block;
    line-height:44px;
    width:44px;
    height:44px;
    text-align:center;
    margin-right:8px;
    border-radius:100%;
    -webkit-transition:all .2s linear;
    -o-transition:all .2s linear;
    transition:all .2s linear
}

.social-icons a:active,.social-icons a:focus,.social-icons a:hover{
    color:#fff;
    background-color:#29aafe
}

.social-icons.size-sm a
{
    line-height:34px;
    height:34px;
    width:34px;
    font-size:14px
}

.social-icons a.facebook:hover{
    background-color:#3b5998
}

.social-icons a.twitter:hover{
    background-color:#00aced
}

.social-icons a.linkedin:hover{
  background-color:#007bb6
}

.social-icons a.instagram:hover{
    background-color:#ea4c89
}

.social-icons a.youtube:hover{
    background-color:#FF0000
}



@media (max-width:767px){

    .social-icons li.title{
        display:block;
        margin-right:0;
        font-weight:600
    }
}

</style>
