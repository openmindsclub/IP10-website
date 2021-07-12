<template>
    <div class="">
        <h2>Conférence & panels</h2>
        <div class="desktop">
            <b-container fluid>
                <b-row align-v="center" align-h="center">
                    <b-col xl="8" lg="10" md="12">
                        <Paragraph :title="conf1.title" :content="conf1.content" :type="conf1.type" time=true :begin="conf1.timeBegin" :end="conf1.timeEnd" :images="conf1.speakers"/>
                    </b-col>
                </b-row>
                <b-row align-v="center" align-h="center">
                    <div class="space2"></div>
                </b-row>
                <b-row  align-h="center">
                    <b-col  xl="5" lg="6" md="12">
                        <transition appear name="come-from-right">
                            <Paragraph :title="conf2.title" :content="conf2.content" :type="conf2.type" time=true :begin="conf2.timeBegin" :end="conf2.timeEnd" :images="conf2.speakers"/>
                        </transition>
                        <div class="space2"></div>
                        <transition appear name="come-from-right">
                            <Paragraph :title="conf3.title" :content="conf3.content" :type="conf3.type" time=true :begin="conf3.timeBegin" :end="conf3.timeEnd" :images="conf3.speakers"/>
                        </transition>
                    </b-col>
                    <b-col  xl="5" lg="6" md="12">
                        <div class="space"></div>
                        <transition appear name="come-from-left">
                            <Paragraph :title="panel1.title" :content="panel1.content" :type="panel1.type" time=true :begin="panel1.timeBegin" :end="panel1.timeEnd" :images="panel1.speakers"/>
                        </transition>
                        <div class="space"></div>
                        <transition appear name="come-from-left">
                            <Paragraph :title="panel2.title" :content="panel2.content" :type="panel2.type" time=true :begin="panel2.timeBegin" :end="panel2.timeEnd" :images="panel2.speakers"/>
                        </transition>
                    </b-col>
                </b-row>
            </b-container>
        </div>
        <div class="mobile">
            <carousel :autoplay="true" :autoplayHoverPause="true" :perPage="1" :loop="true">
                <slide v-for="conf in conferenceAndPanels" :key="conf.tittle" >
                    <Paragraph :title="conf.title" :content="conf.content" :type="conf.type" time=true :begin="conf.timeBegin" :end="conf.timeEnd" :images="conf.speakers"/>
                </slide>
            </carousel>
        </div>
    </div>
</template>

<script>
import Paragraph from '../components/Paragraph.vue';
import { Carousel, Slide } from 'vue-carousel';
export default {
  name: "Sessions",
  components: {
      Carousel,
      Slide,
      Paragraph
  },
  data: () => ({
      slide: 0,
      sliding: null,
      conf1 : {
          title: "La difference entre le libre et l'open source",
          content: "Le libre et l’open source, des concepts frères, mais diffèrent. Pourtant, beaucoup de gens ne font pas la différence entre eux. Dans cette conférence, nous allons donc introduire l’open source, le libre et la différence entre les deux.",
          timeBegin: "9h",
          timeEnd: "9h45",
          type: "Conférence",
          speakers: [
              
          ]
      },
      conf2 : {
          title: "L’open source dans le développement scientifique et les nouvelles technologies",
          content: "L’open source a beaucoup contribué au développement scientifique et nouvelles  technologique durant ces dernières années,  vous découvrirez donc durant cette conférence comment l’open source impacte ces deniers et bien sure l’importance de l’open source dans le progrès humain.",
          timeBegin: "10h",
          timeEnd: "10h45",
          type: "Conférence",
          speakers: [
              {
                  index: 0,
                  name: "Younes Grar",
                  smallDescription: "Consultant IT, expert en ICT.",
                  description: "Consultant IT, expert en ICT et développement de nouveaux business, animateur de la conférence :  L’open source dans le développement scientifique et les nouvelles technologies, et membre du panel, “Avenir de l'open source dans le développement des nouvelles technologies en Algérie et dans le monde”.",
                  image: "speakers/Younes_grar.jpg"
              },
              {
                  index: 5,
                  name: "paul serdigne",
                  smallDescription: "Consultant IT, expert en ICT.",
                  description: "You must mate the king!",
                  image: "speakers/blue.jpg"
              }
          ]
      },
      panel1 : {
          title: "L'impact de l’open source dans le développement des nouvelles technologies en Algérie et dans le monde",
          content: "L’open source a le potentiel de révolutionner le développement de nouvelles technologies en Algérie, il est donc toute a fait naturel pour nous de nous intéresser à cette question. Rejoignez-nous pour ce panel pour en apprendre plus, mais aussi avoir la possibilité de données votre avis.",
          timeBegin: "11h",
          timeEnd: "11h45",
          type: "Panel",
          speakers: [
              {
                  index: 0,
                  name: "Younes Grar",
                  smallDescription: "Consultant IT, expert en ICT.",
                  description: "Consultant IT, expert en ICT et développement de nouveaux business, animateur de la conférence :  L’open source dans le développement scientifique et les nouvelles technologies, et membre du panel, “Avenir de l'open source dans le développement des nouvelles technologies en Algérie et dans le monde”.",
                  image: "speakers/Younes_grar.jpg"
              },
              {
                  index: 1,
                  name: "Idir Nasser BELKEBIR",
                  smallDescription: "Business Owner, business developer, Consultant",
                  description: "Acteur actif, au service du développement des compétences et de la performance des entreprises. Membre du panel  “Avenir de l'open source dans le développement des nouvelles technologies en Algérie et dans le monde”.",
                  image: "speakers/Idir_Nasser_Belkbir1.jpg"
              }
          ]
      },
      conf3 : {
          title: "Géant de l’industrie qui se tourne vers l’open source",
          content: "Google, Facebook, Microsoft  ou encore Amazon, toutes ces entreprises ont une chose en commun, ils se tournent de plus en plus vers des licences open source pour leurs produits. Découvrez avec nous ce que ces géants de l'industrie on a gagné en se tournant vers l’open source.",
          timeBegin: "14h30",
          timeEnd: "15h15",
          type: "Conférence",
          speakers: [
              {
                  index: 2,
                  name: "Rezki DEMIL",
                  smallDescription: "Expert en cybersécurité",
                  description: "Expert en cybersécurité et vivement intéressé par les nouvelles technologies et plateformes open source,  il sera animateur de la conférence : géants de l’industrie qui se tourne vers l’open source, et membre du panel ou nous discuterons sur comment l’open source peut améliorer la croissance des entreprises en Algérie.",
                  image: "speakers/Rezki_DEMIL.jpg"
              },
          ]
      },
      panel2 : {
          title: "Comment l’open source peut améliorer la croissance des entreprises en Algérie",
          content: "De part l’importance économique qu’ont pris les entreprissent se basant sur l’open source ces dernières années, il est intéressant de se poser la question de comment l’open source peut améliorer la croissance des entreprises en Algérie ?",
          timeBegin: "15h30",
          timeEnd: "16h15",
          type: "Panel",
          speakers: [
              {
                  index: 2,
                  name: "Rezki DEMIL",
                  smallDescription: "Expert en cybersécurité",
                  description: "Expert en cybersécurité et vivement intéressé par les nouvelles technologies et plateformes open source,  il sera animateur de la conférence : géants de l’industrie qui se tourne vers l’open source, et membre du panel ou nous discuterons sur comment l’open source peut améliorer la croissance des entreprises en Algérie.",
                  image: "speakers/Rezki_DEMIL.jpg"
              },
              {
                  index: 3,
                  name: "Tarik Zakaria Benmerara",
                  smallDescription: "Entrepreneur, chercheur et contributeur open source",
                  description: "Entrepreneur, chercheur et professeur d'université,  participant à plusieurs projets open source, il est aussi un des fondateurs du club openmindsclub. Membre du panel, “Avenir de l'open source dans le développement des nouvelles technologies en Algérie et dans le monde”.",
                  image: "speakers/Tarik_Zakaria_Benmera.jpg"
              }
          ]
      },
      surprise_speaker : {
          index: 5,
          name: "paul serdigne",
          description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
          image: "speakers/blue.jpg"
      }
  }),
  methods: {
      onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      }
  },
  computed: {
      conferenceAndPanels(){
          return [this.conf1, this.conf2, this.panel1, this.conf3, this.panel2]
      }
  }
};
</script>

<style scoped >
h2{
    color: white;
    font-size: 70px;
    text-align: center;
    margin-top: 60px;
    margin-bottom: 30px;
}

.space{
    height: 4.5em;
}

.space2{
    height: 2em;
}

.desktop{
    display: block;
}

.mobile{
    display: none;
}

@media(max-width: 800px){

    h2{
        font-size: 50px;
    }
}

@media(max-width: 992px){
    .mobile{
        display: block;
    }

    .desktop{
        display: none;
    }
}

/* animations and transitions*/
.come-from-right-enter-active {
    transition: all 0.9s ease-in;
}

.come-from-right-enter {
    opacity: 0;
    transform: translateX(-40%);
}

.come-from-left-enter-active {
    transition: all 0.9s ease-in;
}

.come-from-left-enter {
    opacity: 0;
    transform: translateX(60%);
}

</style>
