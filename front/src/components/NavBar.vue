<template>
<header>
	<nav>
    	<div class="menu-icon" @click="toogleSlideBar()">
        	<i class="fa fa-bars fa-2x"></i>
        </div>
        <div class="menu">
        	<ul v-bind:class="{showing: sidebar}">
				<li v-for="item in items" :key="item.title">
					<a v-if= "!item.composed" :href="item.path">{{ item.title }}</a>
					<div v-else class="dropdown">
  						<p class="dropbtn">{{item.title}}</p>
  						<div class="dropdown-content">
							<a  v-for="subItem in item.components" :key="subItem.title" :href="subItem.path">{{ subItem.title }}</a>
  						</div>
					</div>
				</li>
            </ul>
        </div>
    </nav>
</header>
</template>

<script>
export default {
	name: "NavBar",
	data: () => ({
		sidebar: false,
		items: [
			{ title: "Acceuil", path: "/#/welcome", composed: false},
			{ title: "Event", path: "/#/event", composed: false},
			{ title: "Activities", composed: true, components:[
				{ title: "Conferances", path: "/#/conferences"},
				{ title: "Workshops", path: "/#/workshops"},
				{ title: "Other Activities", path: "/#/activities"},
				{ title: "Stands", path: "/#/stands"}
			]},
			{ title: "Inscriptions", path: "/#/registration", composed: false},
			{ title: "A propos", composed: true, components:[
				{ title: "A propos", path: "/#/about"},
			]},
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

nav ul li p {
    font-family: 'Bungee', cursive;
    text-decoration: none !important;
    color: #4B535C;
    font-size: 18px;
}

nav ul li a:hover{
    color: #E1CF4B;
}

/* Dropdown Button */
.dropbtn {
  border: none;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  color: #F2F5FE;
  position: fixed;
  z-index: 99999;
}

/* Links inside the dropdown */
.dropdown-content a {
  text-decoration: none;
  display: block;
}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
	display: block;
}


nav a.router-link-exact-active {
  text-decoration: underline;
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
