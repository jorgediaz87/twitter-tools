<template>
    <div v-if="profiles !== null">
        <b-container>
            <blockAll :profiles="this.profiles"></blockAll>
        </b-container>
        <b-card-group v-for="rowIdx in Math.ceil(profiles.length / 5)" :key="rowIdx">
            <b-card
                class="card card-profile text-center"
                v-for="profile in profiles.slice(5 * (rowIdx - 1), 5 * rowIdx)"
                :key="profile.id"
            >
                <img class="card-img-top" :src="profile.profile_background_image_url" />
                <div class="card-block">
                    <img alt class="card-img-profile" :src="profile.profile_image_url_https" />
                    <h4 class="card-title">{{ profile.name }}</h4>
                    <small>{{ profile.description }}</small>
                    <div class="card-body">
                        <block-button :profileId="profile.id"></block-button>
                    </div>
                </div>
            </b-card>
        </b-card-group>
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
    animation-name: fade-in;
    animation-fill-mode: both;
    animation-duration: 0.5s;

    $animationDelay: 1;
    @for $i from 1 through 20 {
        .projects div:nth-of-type(#{$i}) {
            animation-delay: #{0.3+ ($i)/30}s;
        }
    }

    @keyframes fade-in {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

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
}
</style>
