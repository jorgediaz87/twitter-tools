<template>
    <div v-if="profiles !== null">
        <div class="container">
            <blockAll :profiles="this.profiles"></blockAll>
        </div>
        <div class="card-group" v-for="rowIdx in Math.ceil(profiles.length / 3)" :key="rowIdx">
            <div
                class="card card-profile text-center"
                v-for="profile in profiles.slice(3 * (rowIdx - 1), 3 * rowIdx)"
                :key="profile.id"
            >
                <img class="card-img-top" :src="profile.profile_background_image_url" />
                <div class="card-block">
                    <img alt class="card-img-profile" :src="profile.profile_image_url_https" />
                    <h4 class="card-title">{{ profile.name }}</h4>
                    <small>{{ profile.description }}</small>
                    <div class="card-body">
                        <block-button
                            :profileName="profile.name"
                            :profileId="profile.id"
                        ></block-button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import BlockAll from './BlockAllComponent';
import BlockButton from './BlockButtonComponent';

export default {
    name: 'card',
    components: {
        BlockAll,
        BlockButton,
    },
    data() {
        return {
            profileId: {
                type: Number,
                default: null,
            },
        };
    },
    props: {
        profiles: {
            type: Array,
            default: null,
        },
    },
    updated() {
        let maxHeight = 0;
        let bios = document.getElementsByTagName('small');
        bios.forEach((bio) => {
            if (bio.offsetWidth > maxHeight) {
                maxHeight = bio.offsetHeight;
            }
        });

        bios.forEach((bio) => {
            bio.style.height = maxHeight;
        });
    },
};
</script>

<style lang="scss">
$bg-start: #9d9181;
$bg-end: #9e866c;
$card-bg: #e6e5e1;
$dribbble-color: #ea4b89;
$twitter-color: #68aade;
$facebook-color: #3b5999;

html {
    min-height: 100%;
    background: linear-gradient($bg-start, $bg-end);
}

body {
    background-color: transparent;
}

.card-profile {
    width: 340px;
    margin: 50px auto;
    background-color: $card-bg;
    border-radius: 0;
    border: 0;
    box-shadow: 1em 1em 2em rgba(0, 0, 0, 0.2);

    .card-img-top {
        border-radius: 0;
        height: 180px;
    }

    .card-img-profile {
        max-width: 100%;
        border-radius: 50%;
        margin-top: -95px;
        margin-bottom: 35px;
        border: 5px solid $card-bg;
    }

    .card-title {
        margin-bottom: 50px;

        small {
            display: block;
            font-size: 0.6em;
            margin-top: 0.2em;
        }
    }

    .card-links {
        margin-bottom: 25px;

        .fa {
            margin: 0 1em;
            font-size: 1.6em;

            &:focus,
            &:hover {
                text-decoration: none;
            }

            &.fa-dribbble {
                color: $dribbble-color;
                font-weight: bold;

                &:hover {
                    color: darken($dribbble-color, 10%);
                }
            }

            &.fa-twitter {
                color: $twitter-color;

                &:hover {
                    color: darken($twitter-color, 10%);
                }
            }

            &.fa-facebook {
                color: $facebook-color;

                &:hover {
                    color: darken($facebook-color, 10%);
                }
            }
        }
    }
}
</style>
