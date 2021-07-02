<template>
    <div id="workshops" class="hero">
        <div class="pricipal-title">
            <h2>Workshops</h2>
        </div>
        <b-container fluid class="page">
            <b-row class="row-class">
                <b-col class="workshop1" md="4" sm="12">
                    <h3>{{workshops[0].title}}</h3>
                    <div class="formation-section">
                        <div class="formation-paragraph">
                            <Paragraph title="" :content="workshops[0].content"/>
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
                        <b-img center :src="require(`../assets/photos/${imageDisplayed.image}`)" fluid :alt="imageDisplayed.alt" :title="imageDisplayed.alt" class="photo"></b-img>
                    </div>
                </b-col>
                <b-col class="workshop2" md="4" sm="12">
                    <h3>{{workshops[1].title}}</h3>
                    <div class="formation-section">
                        <div class="formation-paragraph">
                            <Paragraph title="" :content="workshops[1].content"/>
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
        <div class="space-end"></div>
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
              content: "L'intelligence Artificielle est aujourd’hui présente dans de plus en plus de domaines, donc naturellement avoir des bases en Machine Learning l’un des sous domaines les plus importants de l’IA est aussi de plus en plus important, et c’est justement ce que vous découvrirez dans ce workshop, à savoir comprendre le fonctionnement du Machine learning en utilisant Python.",
              logo_path: 'python.svg',
              alt_image: "python logo",
              formateur: "Ilies CHIBANE",
              description: "Étudiant en ISIL L3 et membre d’OpenMindsCub, il est passionné par l’intelligence artificielle ainsi que le développement de manière général ce qui ont fait le candidat idéal pour animer ce workshop !",
              image: 'python.svg',
          },
          {
              title: "Godot",
              content: "Vous vous êtes toujours intéressé aux jeux vidéos, et vous rêvez d'apprendre à en créer ? Alors ce workshop est fait pour vous ! Vous allez y apprendre à manipuler Godot un moteur de jeux totalement open source ! Peu importe que vous soyez novice ou non, vous êtes le bienvenu pour nous rejoindre et réveiller le game développeur qui sommeille en vous !",
              logo_path: 'godot.png',
              alt_image: "godot logo",
              formateur: "AIT AMARA Mohamed & SOUIDI Mohammed Amine",
              description: "Étudiants en informatique et membres d’OpenMindsCub, passionnés par le développement de nouvelles idées et projets informatiques, ils vous apprendront dans ce workshop à manipuler les bases de godot !",
              image: 'python.svg',
          },
      ],
      actualImage : 0,
      formateurIMG : [
          {
              image: "ilies_photo.png",
              alt: "Ilies CHIBANE"
          },
          {
              image: "mohamed_amine_photo.png",
              alt: "SOUIDI Mohammed Amine"
          },
          {
              image: "ait_amara_mohamed.png",
              alt: "AIT AMARA Mohamed"
          }
      ]
  }),
  methods: {
      getImgUrl(logo_path){
          return  require(logo_path);
      },
      formateur_name(formateur){
          return "Formateur: " + formateur
      },
      change_image(){
          if (this.actualImage == this.formateurIMG.length - 1){
              this.actualImage = 0
          } else {
              this.actualImage++
          }
      }
  },
  computed: {
      imageDisplayed() {
          return this.formateurIMG[this.actualImage]
      }
  },
  mounted: function () {
      window.setInterval(() => {
          this.change_image()
    }, 3000)
}
};
</script>


<style scoped >
.hero{
    background-image: url("../assets/backgrounds/Event_background_3.jpg");

    height: fit-content;
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
    font-size: 40px;
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

.space-end{
    height: 50px;
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

    .row-class{
        width: 100%;
    }
}

</style>
