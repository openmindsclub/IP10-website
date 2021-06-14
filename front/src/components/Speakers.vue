<template>
    <div class="">
        <h2>Conferenciers</h2>
        <carousel-3d :controls-visible="true" :controls-prev-html="'&#10092; '" :controls-next-html="'&#10093;'"
               :controls-width="30" :controls-height="60" :autoplay="true" :autoplay-timeout="6000" :perspective="0" :space="400" :display="3" @after-slide-change="onAfterSlideChange" @before-slide-change="onBeforeSlideChange" @last-slide="onLastSlide">
            <slide v-for="sepeaker in speakers" :key="sepeaker.index" :index="sepeaker.index">
                <figure>
                    <img src="https://picsum.photos/200/300">
                    <figcaption>
                        The sky is the limit only for those who aren't afraid to fly!
                        The sky is the limit only for those who aren't afraid to fly!
                    </figcaption>
                </figure>
            </slide>
        </carousel-3d>
    </div>
</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d';
export default {
    name: "Speakers",
    components: {
        Carousel3d,
        Slide
    },
    data: () => ({
        speakers: [
            {
                index: 0,
                name: "",
                smallDescription: "",
                description: "",
                image: ""
            },
            {
                index: 1,
                name: "",
                smallDescription: "",
                description: "",
                image: ""
            },
            {
                index: 2,
                name: "",
                smallDescription: "",
                description: "",
                image: ""
            },
            {
                index: 3,
                name: "",
                smallDescription: "",
                description: "",
                image: ""
            },
            {
                index: 4,
                name: "",
                smallDescription: "",
                description: "",
                image: ""
            },
            {
                index: 5,
                name: "",
                smallDescription: "",
                description: "",
                image: ""
            }
        ]
    }),
    methods: {
    onAfterSlideChange(index) {
      console.log('@onAfterSlideChange Callback Triggered', 'Slide Index ' + index)
    },
    onBeforeSlideChange(index) {
      console.log('@onBeforeSlideChange Callback Triggered', 'Slide Index ' + index)
    },
    onLastSlide(index) {
      console.log('@onLastSlide Callback Triggered', 'Slide Index ' + index)
    }
  },
};
</script>


<style scoped >
h2{
    color: white;
    font-size: 30px;
    text-align: center;
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

.carousel-3d-controls a {
    color: white;
}
</style>
