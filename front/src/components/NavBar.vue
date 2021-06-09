<template>
<header>
	<nav>
    	<div class="menu-icon" @click="toogleSlideBar()">
        	<i class="fa fa-bars fa-2x"></i>
        </div>
        <div class="menu">
        	<ul v-bind:class="{showing: sidebar}">
				<li v-for="item in items" :key="item.title">
					<a :href="item.path">{{ item.title }}</a>
				</li>
            </ul>
        </div>
    </nav>
</header>
</template>

<script>
export default {
	data: () => ({
		sidebar: false,
		items: [
			{ title: "Event", path: "/#/Event"},
			{ title: "Activités", path: "/#/Activités"},
			{ title: "Inscriptions", path: "/#/Inscriptions"},
			{ title: "A propos", path: "/#/apropos"},
		]
	}),
	methods: {
		toogleSlideBar(){
			this.sidebar = !this.sidebar
		}
	}
};

</script>


<style scoped>

header {
    width: 100%;
}

nav {
    position: fixed;
    width: 100%;
    line-height: 60px;
    z-index: 99999999;
}

nav ul {
    line-height: 45px;
    list-style: none;
    background: rgba(0, 0, 0, 0);
    overflow: hidden;
    color: #4B535C;
    padding: 0;
    text-align: right;
    margin: 0;
}

nav ul li {
    display: inline-block;
    padding: 10px 40px;;
}

nav ul li a {
    font-family: 'Bungee', cursive;
    text-decoration: none !important;
    color: #4B535C;
    font-size: 18px;
}

nav ul li a:hover{
    color: #E1CF4B;
}

.menu-icon {
    line-height: 45px;
    width: 100%;
    background: none;
    text-align: right;
    box-sizing: border-box;
    padding: 10px 30px;
    cursor: pointer;
    color: #fff;
    display: none;
}

@media(max-width: 725px) {
    nav ul {
          max-height: 0px;
          background: #000;
    }

    .showing {
          max-height: 34em;
    }

    nav ul li {
          box-sizing: border-box;
          width: 100%;
          padding: 24px;
          text-align: center;
    }
    nav ul li a {
        font-family: 'Bungee', cursive;
        text-decoration: none !important;
        color: #fff;
        font-size: 18px;
    }
    nav ul li a:hover{
        color: rgb(231, 22, 57);
    }

    .menu-icon {
          display: block;
    }

}
</style>
