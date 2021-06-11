<template>
    <div id="workshops" class="hero">
        <div class="pricipal-title">
            <h2>Workshops</h2>
        </div>
        <b-container fluid class="page">
            <b-row>
                <b-col class="workshop1" md="4" sm="12">
                    <h3>{{workshops[0].title}}</h3>
                    <div class="formation-section">
                        <div class="formation-paragraph">
                            <Paragraph title="Workshop" :content="workshops[0].content"/>
                        </div>
                        <div class="logo">
                            <b-img center :src="require(`../assets/${workshops[0].logo_path}`)" fluid v-bind:alt="workshops[0].alt_image"></b-img>
                        </div>
                        <div class="formateur-paragraph">
                            <Paragraph :title="formateur_name(workshops[0].formateur)" :content="workshops[0].description"/>
                        </div>
                    </div>
                </b-col>
                <b-col class="" md="3" sm="12">
                    <div class="space"></div>
                    <div class="photo-container">
                        <b-img center :src="require('../assets/photos/ilies_photo.png')" fluid alt="jimmy" class="photo"></b-img>
                    </div>
                </b-col>
                <b-col class="workshop2" md="4" sm="12">
                    <h3>{{workshops[1].title}}</h3>
                    <div class="formation-section">
                        <div class="formation-paragraph">
                            <Paragraph title="Workshop" :content="workshops[1].content"/>
                        </div>
                        <div class="logo">
                            <b-img center :src="require(`../assets/${workshops[1].logo_path}`)" fluid v-bind:alt="workshops[1].alt_image"></b-img>
                        </div>
                        <div class="formateur-paragraph">
                            <Paragraph :title="formateur_name(workshops[1].formateur)" :content="workshops[1].description"/>
                        </div>
                    </div>
                </b-col>
            </b-row>
        </b-container>

    </div>
</template>

<script>
import Paragraph from '../components/Paragraph.vue'

export default {
  name: "Workshops",
  components: {
      Paragraph
  },
  data: () => ({
      workshops: [
          {
              title: "Machine Learning avec Python",
              content: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
              logo_path: 'python.svg',
              alt_image: "python logo",
              formateur: "Ilies CHIBANE",
              description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
              image: 'python.svg',
          },
          {
              title: "Godot",
              content: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
              logo_path: 'godot.png',
              alt_image: "godot logo",
              formateur: "AIT AMARA Mohamed & SOUIDI Mohammed Amine",
              description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
              image: 'python.svg',
          },
      ],
  }),
  methods: {
      getImgUrl(logo_path){
          return  require(logo_path);
      },
      formateur_name(formateur){
          return "Formateur: " + formateur
      }
  },
  computed: {

  }
};
</script>


<style scoped >
.hero{
    background-image: url("../assets/backgrounds/Event_background_3.jpg");

    height: 100vh;
    width: 100%;

    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;

    display: flex;
    flex-direction: column;
}

.page{
    padding-left: 10%;
    padding-top:3%;
    padding-right: 3%;
}

h2{
    padding-left: 13%;
    padding-top:4%;
    color: white;
    font-size: 70px;
    text-align: left;
}

h3{
    color: white;
    font-size: 50px;
    text-align: center;
}

.workshop1 .logo{
    width: 30%;
    display: block;
    margin-left: auto;
    margin-right: auto;
}

.workshop2 .logo{
    width: 20%;
    display: block;
    margin-left: auto;
    margin-right: auto;
}

.photo-container{
    width: 110%
}

.space{
    height: 15%;
}

@media(max-width: 1350px){

    h2{
        font-size: 60px;
    }

    h3{
        font-size: 35px;
    }

    .photo-container{
        width: 120%
    }

    .space{
        height: 20%;
    }
}

@media(max-width: 950px){

    h2{
        font-size: 50px;
    }

    h3{
        font-size: 30px;
    }

    .workshop1 .logo{
        width: 50%;
    }

    .workshop2 .logo{
        width: 40%;
    }

    .photo-container{
        width: 125%
    }

    .space{
        height: 30%;
    }
}

@media(max-width: 765px){

    .hero {
        height: fit-content;
        background-repeat: repeat;
    }

    h2{
        padding-top: 8%;
        padding-left: 8%;
        padding-bottom: 8%;
        font-size: 3.8em;
    }

    h3{
        font-size: 40px;
    }

    .workshop1 .logo{
        width: 35%;
    }

    .workshop2 .logo{
        width: 30%;
    }

    .photo-container{
        width: 100%
    }

    .space{
        display: none;
    }
}

</style>
