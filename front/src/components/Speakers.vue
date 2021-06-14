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
                                <img :src="sepeaker.image">
                                <figcaption>
                                    {{sepeaker.smallDescription}}
                                </figcaption>
                            </figure>
                        </slide>
                    </carousel-3d>
                </b-col>
            </b-row>
            <b-row align-v="center" align-h="center">
                <b-col  xl="5" lg="6" md="12">
                    <Paragraph :title="speakers[curent_index].name" :content="speakers[curent_index].description"/>
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
                name: "Aymen Khouas",
                smallDescription: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                image: "https://picsum.photos/200/300"
            },
            {
                index: 1,
                name: "Dovahkiin",
                smallDescription: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                image: "https://picsum.photos/200/300"
            },
            {
                index: 2,
                name: "Link",
                smallDescription: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                image: "https://picsum.photos/200/300"
            },
            {
                index: 3,
                name: "Luck skywalker",
                smallDescription: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                image: "https://picsum.photos/200/300"
            },
            {
                index: 4,
                name: "Jules cesar",
                smallDescription: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                image: "https://picsum.photos/200/300"
            },
            {
                index: 5,
                name: "another random character",
                smallDescription: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                image: "https://picsum.photos/200/300"
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

@media(max-width: 800px){

    h2{
        font-size: 50px;
    }
}
</style>
