<template>
    <div class="paragraph">
        <h3>{{ title }}</h3>
        <img class="large_white_line"  src="../assets/large_white_line.png"/>
        <p>{{ content }}</p>
    </div>
</template>

<script>
export default {
  name: "Paragraph",
  props: ['title', 'content'],
};
</script>


<style scoped >

.paragraph{
    margin: 10px;
    padding: 5px;
}

h3{
    color: white;
    font-size: 25px;
}

p{
    color: white;
    font-size: 15px;
}


.large_white_line {
    width:100%;
    height: 2px;
}

</style>
