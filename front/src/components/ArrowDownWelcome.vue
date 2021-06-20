<template>
    <div class="footer-screen">
        <h6 class="gray-color">{{ title }}</h6>
        <a href="#" class="gray-color"><i class="fas fa-angle-down"></i></a>
    </div>
</template>

<script>
export default {
  name: "ArrowDownWelcome",
  props: ['title'],
};
</script>

<style scoped >

.footer-screen{
    justify-content: center;
    align-items: center;
    padding: 0px;
    height: 90px;
    width: 100%;
    display: flex;
    flex-direction: column;
    position: fixed;
    padding: 10px 10px 10px 10px;
    bottom: 1em;
}

h6{
    font-size: 1em;
    font-weight: bold;
    margin: 0;
    padding: 0;
    position: relative;
    top: 0.9em;
    left: 0.5em;
}

.gray-color {
    color: #4B535C;
}

a{
    line-height:34px;
    height:34px;
    width:34px;
    font-size:4.3em;
    margin: 0;
    padding: 0;
}

@media (max-width: 600px){
    .footer-screen{
        position: relative;
        padding: 0;
        bottom: 3em;
    }
}

</style>
