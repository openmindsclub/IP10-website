<template>
    <footer>
        <b-container fluid>
            <b-row>
                <b-col md="6" sm="12">
                    <h6>Local</h6>
                    <p>CRI, USTHB, Bab Ezzouar, 16111 Bab Ezzouar, Algeria</p>
                </b-col>
                <b-col xs="6" md="3">
                    <h6>Contactez-Nous</h6>
                    <ul class="footer-links">
                        <p>openmindsclub@usthb.dz<br>
                            openmindsclub@gmail.com</p>
                    </ul>
                </b-col>
            </b-row>
            <hr>
        </b-container>
        <b-container fluid>
            <b-row>
                <b-col md="8" sm="6" xs="12">
                    <p class="copyright-text">Made by Humans of
                        <a href="http://openmindsclub.net/" target="_blank">OpenMindsClub</a>.
                    </p>
                </b-col>
                <b-col md="4" sm="6" xs="12">
                    <ul class="social-icons">
                        <li v-for="social_media in social_medias" :key="social_media.title">
                            <a :class="social_media.title" :href="social_media.url" target="_blank"><i :class="social_media.class_image"></i></a>
                        </li>
                        <li></i></a></li>

                    </ul>
                </b-col>
            </b-row>
        </b-container>
    </footer>
</template>

<script>
export default {
	name: "Footer",
    data: () => ({
        social_medias: [
            { title: "facebook", url: "https://www.facebook.com/openmindsclub/", class_image:'fab fa-facebook' },
            { title: "twitter", url: "https://twitter.com/clubopenminds", class_image:'fab fa-twitter'},
            { title: "linkedin", url: "https://www.linkedin.com/company/open-minds-club", class_image:'fab fa-linkedin'},
            { title: "instagram", url: "https://www.instagram.com/openmindsclub/", class_image:'fab fa-instagram'},
            { title: "youtube", url: "https://www.youtube.com/channel/UCTS5jQGSPHuuibdqLUqFAqw", class_image:'fab fa-youtube'},
        ]
    })
};
</script>

<style scoped>
footer
{
  background-color:#000000;
  padding:45px 0 20px;
  font-family: 'Open Sans', sans-serif;
  font-weight: 500;
  line-height:24px;
  color:#7e7d7d;
}
footer hr
{
  border-top-color:#bbb;
  opacity:0.5
}
footer hr.small
{
  margin:20px 0
}
footer h6
{
  color:#fff;
  font-size:16px;
  text-transform:uppercase;
  margin-top:5px;
  letter-spacing:2px
}

.footer-links
{
  padding-left:0;
  list-style:none
}

.footer-links.inline li
{
  display:inline-block
}
footer .social-icons
{
  text-align:right
}
footer .social-icons a
{
  width:40px;
  height:40px;
  line-height:40px;
  margin-left:6px;
  margin-right:0;
  border-radius:100%;
  background-color:#33353d
}
.copyright-text
{
  margin:0
}

.copyright-text a{
    color:#737373;
    text-decoration: none;
}

.copyright-text a:hover{
    color:#ffff;
}
@media (max-width:991px)
{
  footer [class^=col-]
  {
    margin-bottom:30px
  }
}
@media (max-width:767px)
{
  footer
  {
    padding-bottom:0
  }
  footer .copyright-text,.site-footer .social-icons
  {
    text-align:center
  }
}
.social-icons
{
  padding-left:0;
  margin-bottom:0;
  list-style:none
}
.social-icons li
{
  display:inline-block;
  margin-bottom:4px
}
.social-icons li.title
{
  margin-right:15px;
  text-transform:uppercase;
  color:#96a2b2;
  font-weight:700;
  font-size:13px
}
.social-icons a{
  background-color:#eceeef;
  color:#818a91;
  font-size:16px;
  display:inline-block;
  line-height:44px;
  width:44px;
  height:44px;
  text-align:center;
  margin-right:8px;
  border-radius:100%;
  -webkit-transition:all .2s linear;
  -o-transition:all .2s linear;
  transition:all .2s linear
}
.social-icons a:active,.social-icons a:focus,.social-icons a:hover
{
  color:#fff;
  background-color:#29aafe
}
.social-icons.size-sm a
{
  line-height:34px;
  height:34px;
  width:34px;
  font-size:14px
}
.social-icons a.facebook:hover
{
  background-color:#3b5998
}
.social-icons a.twitter:hover
{
  background-color:#00aced
}
.social-icons a.linkedin:hover
{
  background-color:#007bb6
}
.social-icons a.instagram:hover
{
  background-color:#ea4c89
}
@media (max-width:767px)
{
  .social-icons li.title
  {
    display:block;
    margin-right:0;
    font-weight:600
  }
}
</style>
