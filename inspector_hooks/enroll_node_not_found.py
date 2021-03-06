# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ironicclient import exceptions

from ironic_inspector import node_cache
from ironic_inspector import utils


def hook(introspection_data, **kwargs):
    ironic = utils.get_client()
    try:
        node = ironic.node.create(**{'driver': 'fake'})
    except exceptions.HttpError as exc:
        raise utils.Error(_("Can not create node in ironic for unknown"
                            "node: %s") % exc)
    return node_cache.add_node(node.uuid, ironic=ironic)
