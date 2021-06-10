<template>
<div>
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
                    <img @click="Registration()" src="../assets/welcome_screen/participer_button.png" class="participer-button"/>
                </div>
            </div>
            <div class="right-side">
                <img class="clubLogo" src="../assets/omc_logo_grey.png"/>
                <div class = "IPNameLogo sec1">
                    <img class="eventName"  src="../assets/install_party_new_era.png"/>
                    <img class="asset1"  src="../assets/welcome_screen/welcome_special_asset1.png"/>
                    <img class="IPlogo"  src="../assets/logoIP10.png"/>
                </div>
                <div class = "IPNameLogo sec2">
                    <div v-for="pic in pics" :key="pic.title">
                        <img class="socialMedia" :src="getImgUrl(pic.title)" v-bind:alt="pic.title">
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
  name: "Acceuil",
  component: {},
  data: () => ({
      pics: [
          { title: "facebook", path: "/#/acceuil"},
          { title: "twitter", path: "/#/event"},
          { title: "gmail", path: "/#/planning"},
          { title: "instagram", path: "/#/sponsor"},
          { title: "youtube", path: "/#/apropos"},
      ]
  }),
  methods: {
      getImgUrl(pic){
          return  require('../assets/Social_Media_Logos/' + pic + ".png");
      },
      Registration(){
          console.log("clicked")
      }
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
    font-size: 3em;
    color: #4B535C;
    font-weight: bold;
    font-style: italic;
}

.content p{
    font-size: 2em;
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

.socialMedia{
    width:40%;
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


    .IPNameLogo{
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
    }

    .sec1{
        width:auto;
        height: auto;
        margin-top: 10%;
        margin-right: 10%;
        margin-left: 10%;
    }

    .sec2{
        display: none;
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

    .socialMedia{
        width:40%;
    }

}

</style>
