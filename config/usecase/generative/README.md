# Generative AI Rendering

To do a stable diffusion rendering with a depth control, you first need to install the DNN networks as described in the `image-render-generative` readme file. Installing the correct versions of pytorch and all the other modules can be quite difficult. If you run into problems, the module versions as listed in the script `image-render-generative/scripts/get_takuma_diffusers.ps1` should work.

If everything is installed correctly you need to execute the following actions:

- `cathy ws launch -c ./config/usecase/generative -a render`
- `cathy ws launch -c ./config/usecase/generative -a depth`
- `cathy ws launch -c ./config/usecase/generative -a generative`

The parameters of the stable diffusion can be set in the trial file. This generative action will generate 11 images, varying the value of the weight the depth control image should have on the stable diffusion rendering.
