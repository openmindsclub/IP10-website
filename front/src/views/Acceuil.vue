<template>
    <div class="hero-acceuil back-image">
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
                </div>
            </div>
            <div class="right-side">
                <img class="clubLogo" src="../assets/omc_logo_grey.png"/>
                <div class = "IPNameLogo sec1">
                    <img class="eventName"  src="../assets/install_party_new_era.png"/>
                    <img class="asset1"  src="../assets/welcome_special_asset1.png"/>
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
</template>

<script>
import Button from "../components/Button";
export default {
  name: "Acceuil",
  component: {
    Button,
  },
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
      }
  }
};
</script>


<style scoped >
.back-image {
  /* Use "linear-gradient" to add a darken background effect to the image (photographer.jpg). This will make the text easier to read */
  background-image: url("../assets/Index_background_3.jpg");
}

.hero-acceuil {
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
    font-size: 50px;
    font-weight: bold;
    font-style: italic;
}

.content p{
    font-size: 25px;
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
        font-size: 30px;
    }

    .content p{
        font-size: 18px;
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

@media (max-aspect-ratio: 3/2)  {

    .back-image {
      /* Use "linear-gradient" to add a darken background effect to the image (photographer.jpg). This will make the text easier to read */
      background-image: url("../assets/white_shape.jpg");
    }

    .hero-acceuil {
      /* Set a specific height */
      width: 100%;
      /* Position and center the image to scale nicely on all screens */
      background-position: center;
      background-repeat:unset;
      background-size: cover;
      position: relative;
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
        margin-bottom: 10%;
    }

    .IPlogo{
        width:50%;
        height:auto;
        margin-bottom: 20%;
    }

    .asset1{
        display: none;
    }

    .socialMedia{
        width:40%;
    }

}

</style>
