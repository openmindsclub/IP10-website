<template>
<ul>
	<li v-for="item in items" :key="item.title">
		<a :href="item.path">{{ item.title }}</a>
	</li>
					

</ul>
<!-- <div>
  <b-nav  v-for="item in items" :key="item.title">
    <b-nav-item > {{item.title}}</b-nav-item>
  </b-nav>
</div> -->
<!-- <div>
  <b-nav >
    <b-nav-item href="#1">Link 1</b-nav-item>
    <b-nav-item href="#2">Link 2</b-nav-item>
    <b-nav-text>Plain text</b-nav-text>
  </b-nav>
</div> -->
</template>

<script>

export default {
	data: () => ({
		sidebar: false,
		items: [
			{ title: "Acceuil", path: "/#/acceuil"},
			{ title: "Event", path: "/#/event"},
			{ title: "Planning", path: "/#/planning"},
			{ title: "Sponsor", path: "/#/sponsor"},
			{ title: "A propos", path: "/#/apropos"},
		]
	}),
};
</script>

<style scoped>

ul{
	position: absolute;
	width: 100%;
	list-style-type: none;
	display: flex;
	justify-content: flex-end;	
	margin: 0;
	z-index: 2;
	padding: 1.2em;
	margin: 0;
	}
li{
	/* display: inline; */
	padding: 0 10px ;
}
a{
	text-decoration: none;
	color: #4A525C;
}

</style>