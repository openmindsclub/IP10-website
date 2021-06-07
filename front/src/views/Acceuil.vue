<template>
    <div class="container-fluid hero-acceuil">
        <div class="row space2">
            <div class="col-12"></div>
        </div>

        <div class="row">
            <!-- cote gauche -->
            <div class="col-4 text-center">
                <div class="row space1">
                    <div class="col-12"></div>
                </div>
                <div class="row">
                    <div class="col-12">
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                        </p>
                    </div>
                </div>
            </div>
            <div class="col-8">
                <div class="logosAndImages">
                    <img class="clubLogo" src="../assets/omcGreyLogo.png"/>
                    <div class = "IPNameLogo sec1">
                        <img class="eventName"  src="../assets/eventname.png"/>
                        <img class="asset1"  src="../assets/welcomeAsset1.png"/>
                        <img class="IPlogo"  src="../assets/logoIP.png"/>
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
.hero-acceuil {
  /* Use "linear-gradient" to add a darken background effect to the image (photographer.jpg). This will make the text easier to read */
  background-image: url("../assets/Index_background_3.jpg");

  /* Set a specific height */
  height: 100vh;
  width: 100%;
  /* Position and center the image to scale nicely on all screens */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}

.space1{
    height: 35%;
}

.space2{
    height: 8%;
}

p{
    margin-left: 30%;
}

.logosAndImages {
    margin-left: 10%;
    margin-right: 10%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 70vh;
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
    margin-left: 15%;
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

</style>
