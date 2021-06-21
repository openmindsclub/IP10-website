<template>
    <div class="">
        <h2>Conferences & panels</h2>
        <div class="desktop">
            <b-container fluid>
                <b-row align-v="center" align-h="center">
                    <b-col xl="8" lg="10" md="12">
                        <Paragraph :title="conf1.title" :content="conf1.content" time=true :begin="conf1.timeBegin" :end="conf1.timeEnd"/>
                    </b-col>
                </b-row>
                <b-row align-v="center" align-h="center">
                    <div class="space2"></div>
                </b-row>
                <b-row  align-h="center">
                    <b-col  xl="5" lg="6" md="12">
                        <Paragraph :title="conf2.title" :content="conf2.content" time=true :begin="conf2.timeBegin" :end="conf2.timeEnd"/>
                        <div class="space2"></div>
                        <Paragraph :title="conf3.title" :content="conf3.content" time=true :begin="conf3.timeBegin" :end="conf3.timeEnd"/>
                    </b-col>
                    <b-col  xl="5" lg="6" md="12">
                        <div class="space"></div>
                        <Paragraph :title="panel1.title" :content="panel1.content" time=true :begin="panel1.timeBegin" :end="panel1.timeEnd"/>
                        <div class="space"></div>
                        <Paragraph :title="panel2.title" :content="panel2.content" time=true :begin="panel2.timeBegin" :end="panel2.timeEnd"/>
                    </b-col>
                </b-row>
            </b-container>
        </div>
        <div class="mobile">
            <carousel :autoplay="true" :autoplayHoverPause="true" :perPage="1" :loop="true">
                <slide v-for="conf in conferenceAndPanels" :key="conf.tittle" >
                    <Paragraph :title="conf.title" :content="conf.content" time=true :begin="conf.timeBegin" :end="conf.timeEnd"/>
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
          title: "Conferences: La difference entre le libre et l'open source",
          content: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
          timeBegin: "9h",
          timeEnd: "9h45",
      },
      conf2 : {
          title: "Conferences: La difference entre le libre et l'open source",
          content: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
          timeBegin: "9h",
          timeEnd: "9h45",
      },
      conf3 : {
          title: "Conferences: La difference entre le libre et l'open source",
          content: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
          timeBegin: "9h",
          timeEnd: "9h45",
      },
      panel1 : {
          title: "Panel: La difference entre le libre et l'open source",
          content: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
          timeBegin: "9h",
          timeEnd: "9h45",
      },
      panel2 : {
          title: "Panel: La difference entre le libre et l'open source",
          content: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
          timeBegin: "9h",
          timeEnd: "9h45",
      },
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
</style>
