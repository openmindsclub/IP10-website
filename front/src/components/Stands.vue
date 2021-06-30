<template>
    <div id="stands" class="hero">
        <b-container fluid class="page">
            <b-row class="row-class">
                <b-col class="club-stands" md="5" sm="12">
                    <h3>Stands</h3>
                    <div class="stand" v-for="stand in stands" :key="stand.stand_title">
                        <Paragraph :title="stand.stand_title" :content="stand.content"/>
                    </div>
                </b-col>
                <b-col class="instalation" md="6" sm="12">
                    <h3>Installations GNU/Linux</h3>
                    <div class="distribution-paragraph">
                        <Paragraph title="Les Distributions disponibles" content="Comme chaque année et comme toute Install Party qui se respecte, nous vous offrant d'installer GNU/Linux sur vos machines, nous proposant des multitudes de distributions que nous même utilisons dans notre quotidien, si vous êtes intéressé à faire le pas, n’hésiter pas à nous y rejoindre."/>
                    </div>
                    <div class="logos">
                        <div class="logo" v-for="distribution in distributions" :key="distribution.dist_name">
                            <b-img center :src="require(`../assets/${distribution.logo}`)" fluid v-bind:alt="distribution.dist_name"></b-img>
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
  name: "Stands",
  components: {
      Paragraph
  },
  data: () => ({
      distributions: [
          { dist_name: "Ubuntu", logo: "ubuntu.svg.png" },
          { dist_name: "Linux Mint", logo: "Linux_Mint.svg.png" },
          { dist_name: "Monjaro", logo: "Manjaro-logo.svg.png" }
      ],
      stands: [
          { stand_title: "Stand des Alternatifs", content: "De nos jours l’open source et de plus en plus présent et certains produits sont même devenu incontournable, mais beaucoup d’autre manque encore de visibilité malgré une qualité Exceptionnel. Rendez-nous donc visite au stand des alternatives pour découvrir des produits open source qu’ils soient connue ou non." },
          { stand_title: "Presentation des distributions", content: "GNU/Linux étant au cœur de l’événement, il est donc tous a fait naturel pour nous de proposer un stand consacré aux distributions linux, ou vous découvrirez le point fort, les fonctionnalité et fonctionnement de certaines distributions. Que vous ayez envie d’en apprendre plus sur une distribution avant de faire le pas ou  que vous soyez simplement curieux, vous êtes invité à nous y rejoindre." },
          { stand_title: "OMC Projects", content: "Entre Projets informatiques, Arduino, magazines, nous avons créé chez OpenMindsCub une variété de produit et de projets, Rendez nous donc visite à notre stand pour découvrir ces derniers et en apprendre plus sur le club et sa philosophie." }
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
};
</script>


<style scoped >
.hero{
    background-image: url("../assets/backgrounds/Event_background_4.jpg");

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
    padding-top:8%;
    padding-right: 3%;
}



h3{
    color: white;
    font-size: 50px;
    text-align: center;
}

.logos{
    display: flex;
    justify-content: space-around;
    align-items: center;
}

.logo{
    width: 20%;
}

@media(max-width: 1500px){

    .hero {
        height: fit-content;
        background-repeat: repeat;
    }
}

@media(max-width: 765px){

    .hero {
        height: fit-content;
        background-repeat: repeat;
    }

    .logos{
        padding-bottom:8%;
    }

    .row-class{
        width: 100%;
    }
}

</style>
