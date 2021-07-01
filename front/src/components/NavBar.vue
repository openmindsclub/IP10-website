<template>
<header>
	<nav>
		<div class="logo-box">
			<router-link :to="items[0].path"><img class="logo"  src="../assets/logoIP10.png"/></router-link>
		</div>
    	<div class="menu-icon" :class="[menuTheme, {showing: sidebar}]">
        	<i class="fa fa-bars fa-2x" @click="toogleSlideBar()"></i>
        </div>
        <div class="menu">
        	<ul class="ul-principal" v-bind:class="[backgroundTheme, {showing: sidebar}]">
				<li v-for="item in items" :key="item.title">
					<router-link v-if= "item.route" :to="item.path">{{ item.title }}</router-link>
					<div v-else>
						<a v-if= "!item.composed" :href="item.path">{{ item.title }}</a>
						<div v-else class="dropdown">
							<button class="dropbtn">{{item.title}}
	      						<i class="fa fa-caret-down"></i>
	    					</button>
	  						<ul class="dropdown-content">
								<li v-for="subItem in item.components" :key="subItem.title">
									<a :href="subItem.path">{{ subItem.title }}</a>
								</li>
	  						</ul>
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
	props: ['route'],
	data: () => ({
		sidebar: false,
		items: [
			{ title: "Acceuil", route:true, path: "/", composed: false},
			{ title: "Home", route:true, path: "Home", composed: false},
			{ title: "Activities", route:false, composed: true, components:[
				{ title: "Conférence", path: "Home#conferences"},
				{ title: "Workshops", path: "Home#workshops"},
				{ title: "Other Activities", path: "Home#activities"},
				{ title: "Stands", path: "Home#stands"}
			]},
			{ title: "Inscriptions", route:true, path: "Registration", composed: false},
			{ title: "Sponsor", route:false, composed: false, path: "Home#sponsor"},
		]
	}),
	methods: {
		toogleSlideBar(){
			this.sidebar = !this.sidebar
		}
	},
	computed: {
		backgroundTheme() {
			if (this.route == "welcome"){
				return "welcome-background"
			} else if (this.route == "home") {
				return "home-background"
			} else if (this.route == "registration") {
				return "registration-background"
			}
		},
		menuTheme() {
			if (this.route == "welcome"){
				return "welcome-menu"
			} else if (this.route == "home") {
				return "home-menu"
			} else if (this.route == "registration") {
				return "registration-menu"
			}
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
    line-height: 30px;
    z-index: 99999999;

}

.logo{
	width: 35px;
	position: fixed;
	margin-left: 15px;
	margin-top: 13px;
}

.ul-principal {
    line-height: 35px;
    list-style: none;
    overflow: hidden;
    text-align: right;
}

.ul-principal li {
    display: inline-block;
    padding: 10px 30px;
}

.ul-principal li a {
    font-size: 20px;
}

.dropbtn {
    color: #4B535C;
	background: rgba(0, 0, 0, 0);
    font-size: 20px;
	border: none;
  	outline: none;
}

nav ul li a:hover{
    color: #E1CF4B;
}

.dropdown {
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: fixed;
  padding: 20px;
  z-index: 99999;
}


.dropdown-content li {
	display: block;
    text-align: left;
}

/* Links inside the dropdown */
.dropdown-content a {
  padding-top: 10px;
}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
	display: block;
}

.dropdown:hover .dropbtn {
	color: #E1CF4B;
}

.menu-icon {
    line-height: 45px;
    width: 100%;
    box-sizing: border-box;
    padding: 10px 30px;
    cursor: pointer;
    color: #fff;
    display: none;
}

/* welcome screen */
.welcome-background{
	background: #F2F5FE;
}

.welcome-background a{
    color: #4B535C;
}

.welcome-background .dropbtn{
    color: #4B535C;
}

.welcome-background .dropdown-content {
  background: #F2F5FE;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
}

.welcome-menu {
    background: #F2F5FE;
}

/* home screen */
.home-background{
	background: #41494C;
}

.home-background a{
    color: white;
}

.home-background .dropbtn{
    color: white;
}

.home-background .dropdown-content {
  background: #41494C;
}

.home-menu {
    background: #41494C;
}

/* registration screen */
.registration-background{
	background: rgba(0, 0, 0, 0);
}

.registration-background a{
    color: white;
}

.registration-background .dropbtn{
    color: white;
}

.registration-background .dropdown-content {
  background: #41494C;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
}

.registration-menu {
    background: none;
}

@media(max-width: 725px) {

	.logo{
		position: absolute;
		right: 0px;
		margin-left: 0px;
		margin-right: 15px;
	}

    .ul-principal {
    	max-height: 0px;
    }

    .showing {
        max-height: fit-content;
    }

    .ul-principal li {
        box-sizing: border-box;
        width: 100%;
        padding-top: 15px;
		padding-bottom: 15px;
		display: flex;

    }

    .ul-principal li a {
        font-size: 20px;
    }

    li a:hover{
        color: #E1CF4B;
    }

    .menu-icon {
          display: block;
    }

	.dropdown-content{
	  	padding: 0px;
		box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
	}

	.dropdown-content a {
	  padding-top: 4px;
	  font-size: 12px;
	}

	.dropbtn {
	    padding: 0px;
	}

	.registration-background .dropdown-content {
	  box-shadow: none;
	}

	.welcome-background {
        background: #F2F5FE;
		box-shadow: 0px 0px 0px 0px rgba(0,0,0,0.2);
    }

	.home-background {
        background: #41494C;
    }

	.registration-background {
        background: #41494C;
    }

	.registration-menu.showing {
	    background: #41494C;
	}

}



</style>
