<template>
    <div class="">
        <h2>Conferenciers</h2>
        <b-container fluid>
            <b-row align-v="center" align-h="center">
                <b-col xl="6" lg="10" md="12">
                    <carousel-3d :controls-visible="true" :controls-prev-html="'&#10092; '" :controls-next-html="'&#10093;'"
                           :controls-width="30" :controls-height="60" :autoplay="true" :autoplay-timeout="6000" :perspective="0" :space="400" :display="3" @after-slide-change="onAfterSlideChange">
                        <slide v-for="sepeaker in speakers" :key="sepeaker.index" :index="sepeaker.index">
                            <figure>
                                <img :src="require(`../assets/${sepeaker.image}`)">
                                <figcaption>
                                    {{sepeaker.smallDescription}}
                                </figcaption>
                            </figure>
                        </slide>
                    </carousel-3d>
                </b-col>
            </b-row>
            <b-row class="speaker-content" align-v="center" align-h="center">
                <b-col  xl="5" lg="6" md="12">
                    <transition name="change-speaker" mode="out-in">
                        <Paragraph :title="speakers[curent_index].name" :content="speakers[curent_index].description"/>
                    </transition>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d';
import Paragraph from '../components/Paragraph.vue';
export default {
    name: "Speakers",
    components: {
        Carousel3d,
        Slide,
        Paragraph
    },
    data: () => ({
        curent_index : 0,
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
                name: "Rezki DEMIL",
                smallDescription: "Expert en cybersécurité",
                description: "Expert en cybersécurité et vivement intéressé par les nouvelles technologies et plateformes open source et sa conférence sera sur les géants de l’industrie qui se tourne vers l’open source, puis sera membre du panel ou nous discuterons comment l’open source peut améliorer la croissance des entreprises en Algérie.",
                image: "speakers/Rezki_DEMIL.jpg"
            },
            {
                index: 2,
                name: "Tarik Zakaria Benmerara",
                smallDescription: "Entrepreneur, chercheur et contributeur open source",
                description: "Entrepreneur, chercheur et professeur d'université,  participant à plusieurs projets open source, il est aussi un des fondateurs du club openmindsclub. Membre du panel, “Avenir de l'open source dans le développement des nouvelles technologies en Algérie et dans le monde”.",
                image: "speakers/Tarik_Zakaria_Benmera.jpg"
            },
            {
                index: 3,
                name: "Idir Nasser BELKEBIR",
                smallDescription: "Business Owner, business developer, Consultant",
                description: "Acteur actif, au service du développement des compétences et de la performance des entreprises. Membre du panel  “Avenir de l'open source dans le développement des nouvelles technologies en Algérie et dans le monde”.",
                image: "speakers/Idir_Nasser_Belkbir1.jpg"
            }
        ]
    }),
    methods: {
    onAfterSlideChange(index) {
        this.curent_index = index
    },
  },
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

.carousel-3d-container figure {
  margin:0;
}

.carousel-3d-container figcaption {
  position: absolute;
  background-color: rgba(0, 0, 0, 0.5);
  color: #fff;
  bottom: 0;
  position: absolute;
  bottom: 0;
  padding: 15px;
  font-size: 12px;
  min-width: 100%;
  box-sizing: border-box;
}

.speaker-content{
    height: 300px;
}

@media(max-width: 800px){

    h2{
        font-size: 50px;
    }
}


/* animations and transitions*/
.change-speaker-leave-active, .change-speaker-enter-active {
    transition: opacity 0.9s ease-in;
}

.change-speaker-leave-to, .change-speaker-enter-from {
    opacity: 0;
}

</style>
