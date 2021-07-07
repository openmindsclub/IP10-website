<template>
    <div class="paragraph">
        <h4 :class="text_color">{{ title }}</h4>
        <img class="large-line" :class="show_white_line" src="../assets/large_white_line.png"/>
        <img class="large-line" :class="show_gray_line" src="../assets/large_gray_line.png"/>
        <div v-if="time">
            <h6 class="time" :class="text_color">{{type}} : {{begin}} - {{end}}</h6>
            <div v-if="images.length > 0" class="images">
                <div v-for="speaker in images" :key="speaker.index" >
                    <b-img class="image" rounded="circle" :src="speaker.image" :alt="speaker.name" :title="speaker.name" @click="showModal(speaker.index)"></b-img>
                </div>
            </div>
        </div>
        <p :class="text_color">{{ content }}</p>
        <b-modal v-model="showModalBool" centered :title="modalHeader">
            <p>{{modalContent}}</p>
            <div class="modal-contener">
                <b-img class="modal-image" rounded="circle" :src="modalImage" :alt="modalHeader" :title="modalHeader"></b-img>
            </div>
        </b-modal>
    </div>
</template>

<script>
export default {
  name: "Paragraph",
  props: ['title', 'content', 'color', 'time', 'begin', 'end', 'type', 'images'],
  data: () => ({
      showModalBool: false,
      modalContent: "",
      modalImage: "",
      modalHeader: "",
  }),
  methods: {
            showModal(id) {
                console.log(id)
                console.log(this.images)
                for (let image of this.images){
                    if (image.index == id){
                        console.log(image.index)
                        console.log(id)
                        this.modalContent = image.description
                        this.modalImage = image.image
                        this.modalHeader = image.name
                        console.log(this.modalContent)
                    }
                }
                this.showModalBool = true
            },
            hideModal() {
                this.showModalBool = false
            },
  },
  computed: {
      text_color(){
          if (this.color === 'gray'){
              return 'gray-color'
          } else {
              return 'white-color'
          }
      },
      show_white_line(){
          if (this.color === 'gray'){
              return 'dont-display-line'
          } else {
              return 'display-line'
          }
      },
      show_gray_line(){
          if (this.color === 'gray'){
              return 'display-line'
          } else {
              return 'dont-display-line'
          }
      }
  }
};
</script>


<style scoped >

.paragraph{
    margin: 10px;
    padding: 5px;
}

h4{
    font-size: 30px;
}

p{
    font-size: 17px;
}

.time{
    padding-top: 10px;
    font-size: 15px;
    font-weight: normal;
    font-style: italic;
}

.white-color {
    color: white;
}

.gray-color {
    color: #4B535C;
}

.large-line {
    width:100%;
    height: 2px;
}

.display-line {
    display: block;
}

.dont-display-line {
    display: none;
}

.images{
    display: flex
}

.image{
    width: 30px;
    height: 30px;
    margin-right: 5px;
}

.modal-image{
    width: 300px;
    height: 300px;
}

.modal-contener{
    display: flex;
    justify-content: center;
}


@media(max-width: 992px){
    .modal-image{
        width: 250px;
        height: 250px;
    }
}

@media(max-width: 800px){

    .modal-image{
        width: 150px;
        height: 150px;
    }
}

@media(max-width: 600px){

    .modal-image{
        width: 100px;
        height: 100px;
    }
}


</style>
