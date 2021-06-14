<template>
    <div class="paragraph">
        <h4 :class="text_color">{{ title }}</h4>
        <img class="large-line" :class="show_white_line" src="../assets/large_white_line.png"/>
        <img class="large-line" :class="show_gray_line" src="../assets/large_gray_line.png"/>
        <p :class="text_color">{{ content }}</p>
    </div>
</template>

<script>
export default {
  name: "Paragraph",
  props: ['title', 'content', 'color'],
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
</style>
